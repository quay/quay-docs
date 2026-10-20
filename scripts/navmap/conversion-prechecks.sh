#!/usr/bin/env bash
#
# conversion-prechecks.sh - Automated AsciiDoc pre-conversion validation for Red Hat Quay
#
# Runs three validation checks:
# 1. Map completeness (asciidoctor)
# 2. Vale DITA style validation
# 3. Exploration (Vale suggestions)
#
# Usage:
#   ./conversion-prechecks                           # Check quay navigation
#   ./conversion-prechecks quay                      # Check quay navigation
#   ./conversion-prechecks <category>                # Check one quay category map
#   ./conversion-prechecks maps/quay/configure.adoc  # Check a specific map file
#   ./conversion-prechecks --all                     # Check all products

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

# Available products
AVAILABLE_PRODUCTS=(quay)
DITA_CONFIG="${DITA_CONFIG:-$HOME/.dita.ini}"

# Check prerequisites
check_prerequisites() {
    local missing=()

    if ! command -v asciidoctor &>/dev/null; then
        missing+=("asciidoctor (gem install asciidoctor)")
    fi

    if ! command -v list-content &>/dev/null; then
        missing+=("list-content (gem install asciidoctor-list-content)")
    fi

    if ! command -v vale &>/dev/null; then
        missing+=("vale (https://docs.vale.sh/topics/installation)")
    fi

    if [ ! -f "$DITA_CONFIG" ]; then
        missing+=("${DITA_CONFIG} (AsciiDocDITA Vale configuration)")
    fi

    if [ ${#missing[@]} -gt 0 ]; then
        echo -e "${RED}ERROR: Missing prerequisites:${NC}"
        printf '  - %s\n' "${missing[@]}"
        echo ""
        echo -e "${YELLOW}Please install missing tools before running conversion pre-checks.${NC}"
        exit 1
    fi
}

# Get log file name
get_log_file() {
    local product=$1
    local log_type=$2
    local category=$3

    if [ -n "$category" ]; then
        echo "logs/${category}-${log_type}.log"
    else
        echo "logs/${log_type}.log"
    fi
}

# Run check 1: Map completeness
check_map_completeness() {
    local product=$1
    local nav_file=$2
    local category=$3
    local log_file
    log_file=$(get_log_file "$product" "asciidoctor" "$category")
    : > "$log_file" || return 1

    echo -e "${BLUE}[1/3] Checking map completeness for ${product}${category:+/$category}...${NC}"

    if [ ! -f "$nav_file" ]; then
        echo "ERROR: Navigation file not found: ${nav_file}" >> "$log_file"
        echo -e "${RED}  ERROR: Navigation file not found: ${nav_file}${NC}"
        return 1
    fi

    local temp_output="$WORK_DIR/asciidoctor.out"

    local asciidoctor_status=0
    asciidoctor -o /dev/null "$nav_file" > "$temp_output" 2>&1 || asciidoctor_status=$?

    if [ "$asciidoctor_status" -ne 0 ]; then
        cat "$temp_output" > "$log_file" || return 1
        echo "ERROR: Asciidoctor exited with status ${asciidoctor_status}" >> "$log_file"
        echo -e "${RED}  ERROR: Asciidoctor exited with status ${asciidoctor_status} - see ${log_file}${NC}"
        return 1
    fi

    if ! awk '/ERROR/' "$temp_output" > "$log_file"; then
        echo -e "${RED}  ERROR: Could not write ${log_file}${NC}"
        return 1
    fi

    if [ -s "$log_file" ]; then
        local error_count
        error_count=$(grep -c ERROR "$log_file")
        echo -e "${RED}  ✗ Found ${error_count} error(s) - see ${log_file}${NC}"
        return 1
    else
        echo -e "${GREEN}  ✓ No errors found${NC}"
        return 0
    fi
}

# Discover content once per target and preserve failures for both Vale checks.
prepare_content() {
    local nav_file=$1
    local temp_list="$WORK_DIR/content.list"
    : > "$WORK_DIR/content-errors.log" || return 1
    if ! list-content "$nav_file" > "$temp_list" 2> "$WORK_DIR/content-errors.log"; then
        echo "ERROR: list-content failed for ${nav_file}" >> "$WORK_DIR/content-errors.log"
        return 1
    fi
    if ! sort -u "$temp_list" -o "$temp_list"; then
        echo "ERROR: Could not sort content for ${nav_file}" >> "$WORK_DIR/content-errors.log"
        return 1
    fi
    if [ ! -s "$temp_list" ]; then
        echo "ERROR: No content files found for ${nav_file}" >> "$WORK_DIR/content-errors.log"
        return 1
    fi
    local content_file
    while IFS= read -r content_file || [ -n "$content_file" ]; do
        [ -n "$content_file" ] || continue
        printf '%s\0' "$content_file" || return 1
    done < "$temp_list" > "$WORK_DIR/content.nul"
    if [ ! -s "$WORK_DIR/content.nul" ]; then
        echo "ERROR: No content files found for ${nav_file}" >> "$WORK_DIR/content-errors.log"
        return 1
    fi
}

# Run a Vale check.
check_vale() {
    local product=$1
    local category=$2
    local log_type=$3
    local content_status=$4
    local log_file
    log_file=$(get_log_file "$product" "$log_type" "$category")
    : > "$log_file" || return 1
    local vale_args=(--config "$DITA_CONFIG" --output line --no-exit)
    if [ "$log_type" == "exploration" ]; then
        echo -e "${BLUE}[3/3] Running exploration check for ${product}${category:+/$category}...${NC}"
        vale_args+=(--filter '.Level=="suggestion"')
    else
        echo -e "${BLUE}[2/3] Running Vale DITA validation for ${product}${category:+/$category}...${NC}"
    fi
    if [ "$SYNC_STATUS" -ne 0 ]; then
        cat "$WORK_DIR/vale-sync.log" >> "$log_file" || return 1
        echo "ERROR: Vale style synchronization failed" >> "$log_file"
    fi
    if [ "$content_status" -ne 0 ]; then
        cat "$WORK_DIR/content-errors.log" >> "$log_file" || return 1
    fi
    if [ "$SYNC_STATUS" -ne 0 ] || [ "$content_status" -ne 0 ]; then
        echo -e "${RED}  ERROR: Could not prepare Vale validation - see ${log_file}${NC}"
        return 1
    fi
    if ! xargs -0 vale "${vale_args[@]}" < "$WORK_DIR/content.nul" > "$log_file" 2>&1; then
        echo "ERROR: Vale execution failed" >> "$log_file"
        echo -e "${RED}  ERROR: Vale execution failed - see ${log_file}${NC}"
        return 1
    fi
    if [ -s "$log_file" ]; then
        echo "  Summary of issues found:"
        cut -d : -f 4 "$log_file" | sort | uniq -c | sort -rn | sed 's/^/    /'
        echo -e "${YELLOW}  ⚠ Issues logged - see ${log_file}${NC}"
        if [ "$log_type" != "exploration" ]; then
            return 1
        fi
        if grep -q "AttributeDefinition" "$log_file"; then
            echo -e "${YELLOW}  ⚠ Found problematic AttributeDefinition - review required${NC}"
        fi
        if grep -q "SnippetLink" "$log_file"; then
            echo -e "${YELLOW}  ℹ Found SnippetLink - may need post-conversion cleanup${NC}"
        fi
    else
        echo -e "${GREEN}  ✓ No issues found${NC}"
    fi
    return 0
}

# Run checks for a single product or category
run_checks_for_product() {
    local product=$1
    local nav_file=$2
    local category=$3
    local status=0

    local check_target="$product"
    if [ -n "$category" ]; then
        check_target="${product}/${category}"
    fi

    echo -e "\n${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${GREEN}Running pre-checks for: ${check_target}${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

    check_map_completeness "$product" "$nav_file" "$category" || status=1
    echo ""
    local content_status=0
    prepare_content "$nav_file" || content_status=1
    check_vale "$product" "$category" vale "$content_status" || status=1
    echo ""
    check_vale "$product" "$category" exploration "$content_status" || status=1

    echo ""
    if [ $status -eq 0 ]; then
        echo -e "${GREEN}✓ All critical checks passed for ${check_target}${NC}"
    else
        echo -e "${RED}✗ Some checks failed for ${check_target} - review logs${NC}"
    fi

    return $status
}

# Main execution
main() {
    local check_items=()
    local overall_status=0

    if [ "$#" -gt 1 ]; then
        echo "Usage: conversion-prechecks [product|category|maps/quay/file.adoc|--all]" >&2
        exit 2
    fi
    if [ "${1:-}" == "--help" ] || [ "${1:-}" == "-h" ]; then
        echo "Usage: conversion-prechecks [product|category|maps/quay/file.adoc|--all]"
        echo ""
        echo "Examples:"
        echo "  ./conversion-prechecks                  # Check quay navigation"
        echo "  ./conversion-prechecks quay             # Check quay navigation"
        echo "  ./conversion-prechecks configure        # Check quay/configure category"
        echo "  ./conversion-prechecks --all            # Check all products"
        echo ""
        echo "Available quay categories:"
        ls maps/quay/*.adoc 2>/dev/null | grep -v navigation.adoc | xargs -n1 basename | sed 's/\.adoc$//' | sed 's/^/  /'
        return 0
    fi

    # Parse arguments
    if [ $# -eq 0 ]; then
        # Default: check quay navigation
        check_items+=("quay:maps/quay/navigation.adoc:")
    elif [ "$1" == "--all" ]; then
        for product in "${AVAILABLE_PRODUCTS[@]}"; do
            if [ -f "maps/${product}/navigation.adoc" ]; then
                check_items+=("${product}:maps/${product}/navigation.adoc:")
            fi
        done
    else
        local arg="$1"

        if [ -f "maps/${arg}/navigation.adoc" ]; then
            # Exact product name
            check_items+=("${arg}:maps/${arg}/navigation.adoc:")
        elif [ -f "maps/quay/${arg}.adoc" ]; then
            # Category name without extension
            check_items+=("quay:maps/quay/${arg}.adoc:${arg}")
        elif [ -f "maps/quay/${arg}" ]; then
            # Category with .adoc extension
            local category
            category=$(basename "$arg" .adoc)
            check_items+=("quay:maps/quay/${arg}:${category}")
        elif [ -f "$arg" ] && [[ "$arg" == maps/* ]]; then
            # Full path to a map file
            local product category
            product=$(echo "$arg" | cut -d/ -f2)
            category=$(basename "$arg" .adoc)
            if [ "$category" == "navigation" ]; then
                check_items+=("${product}:${arg}:")
            else
                check_items+=("${product}:${arg}:${category}")
            fi
        else
            echo -e "${RED}ERROR: Could not find map file for: ${arg}${NC}"
            echo ""
            echo "Available products: ${AVAILABLE_PRODUCTS[*]}"
            echo ""
            echo "Available quay categories:"
            ls maps/quay/*.adoc 2>/dev/null | grep -v navigation.adoc | xargs -n1 basename | sed 's/\.adoc$//' | sed 's/^/  /'
            exit 1
        fi
    fi

    if [ "${#check_items[@]}" -eq 0 ]; then
        echo "ERROR: No navigation maps found" >&2
        return 1
    fi

    echo -e "${BLUE}AsciiDoc Pre-Conversion Checks${NC}"
    echo -e "${BLUE}===============================${NC}"

    check_prerequisites

    mkdir -p logs || return 1
    WORK_DIR=$(mktemp -d "${TMPDIR:-/tmp}/conversion-prechecks.XXXXXX") || return 1
    trap 'rm -rf -- "$WORK_DIR"' EXIT
    SYNC_STATUS=0
    echo "Syncing Vale styles..."
    vale --config "$DITA_CONFIG" sync > "$WORK_DIR/vale-sync.log" 2>&1 || SYNC_STATUS=$?
    cat "$WORK_DIR/vale-sync.log"

    echo ""

    for item in "${check_items[@]}"; do
        IFS=':' read -r product nav_file category <<< "$item"
        if ! run_checks_for_product "$product" "$nav_file" "$category"; then
            overall_status=1
        fi
    done

    # Final summary
    echo -e "\n${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}Summary${NC}"
    echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

    echo "Log files created:"
    for item in "${check_items[@]}"; do
        IFS=':' read -r product nav_file category <<< "$item"

        local display_name="$product"
        if [ -n "$category" ]; then
            display_name="${product}/${category}"
        fi

        echo "  ${display_name}:"

        local log_type log_file
        for log_type in asciidoctor vale exploration; do
            log_file=$(get_log_file "$product" "$log_type" "$category")
            if [ -f "$log_file" ]; then
                ls -lh "$log_file" | awk '{print "    " $9 " (" $5 ")"}'
            fi
        done
    done

    echo ""
    if [ $overall_status -eq 0 ]; then
        echo -e "${GREEN}✓ All products passed critical checks${NC}"
    else
        echo -e "${RED}✗ Some products have issues - review logs and fix before conversion${NC}"
    fi

    exit $overall_status
}

main "$@"
