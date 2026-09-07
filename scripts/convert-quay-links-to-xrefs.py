#!/usr/bin/env python3
"""Convert docs.redhat.com and access.redhat.com red_hat_quay links in modules/ to JTBD xrefs."""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
MODULES = REPO / "modules"
JTBD = REPO / "quay_jtbd"

LEGACY_BOOK_MAP = {
    "red_hat_quay_api_reference": "reference",
    "red_hat_quay_api_guide": "develop",
    "configure_red_hat_quay": "configure",
    "securing_red_hat_quay": "secure",
    "upgrade_red_hat_quay": "upgrade",
    "deploying_the_red_hat_quay_operator_on_openshift_container_platform": "install",
    "red_hat_quay_operator_features": "optimize",
    "builders_and_image_automation": "develop",
    "use_red_hat_quay": "administer",
    "manage_red_hat_quay": None,
    "vulnerability_reporting_with_clair_on_red_hat_quay": "configure",
    "red_hat_quay_release_notes": "whats_new",
    "release_notes": "whats_new",
    "proof_of_concept_-_deploying_red_hat_quay": "install",
    "managing_access_and_permissions": "secure",
    "red_hat_quay_architecture": "discover",
    "troubleshooting_red_hat_quay": "troubleshoot",
    "deploy_red_hat_quay_-_high_availability": "plan",
}

# Legacy anchors that should resolve to the book landing page (no fragment).
BOOK_LANDING_ANCHORS = frozenset({"doc-wrapper"})

# Bare product doc hub URLs (no legacy book slug).
PRODUCT_DOC_CATEGORY = "discover"

# Legacy anchor ID -> JTBD module anchor ID
ANCHOR_REMAP = {
    "restoreta": "restoretag",
    "monitoring-single-namespace": "operator-unmanaged-monitoring",
    "operator-preconfig-tls-routes": "configuring-ssl-tls-routes",
    "operator-disabling-hpa": "operator-hpa-overview",
    "overriding-cluster-tls-security-profile": "operator-ocp-tls-security-profile",
    "config-fields-misc": "config-fields-web-ui",
    "repo-mirroring-in-red-hat-quay": "arch-mirroring-intro",
    "quay-bridge-operator": "quay-bridge-operator-features",
    "preserving-tls-settings-operator-upgrade_upgrade-quay-v3": (
        "preserving-tls-settings-operator-upgrade_upgrade_red_hat_quay_on_openshift_container_platform"
    ),
    "operator-ipv6-dual-stack": "proc_manage-ipv6-dual-stack",
    "configuring-oidc-authentication": "configuring-entra-oidc",
    "preparing_for_red_hat_quay_high_availability": "preparing-for-quay-ha",
    "set_up_ceph": "set-up-ceph",
    "red_hat_quay_garbage_collection": "garbage-collection",
    "tag-expiration": "setting-tag-expiration-using-ui",
    "using-ssl-to-protect-quay": "ssl-tls-quay-overview",
    "clair-v4": "clair-vulnerability-scanner",
    "clair-vulnerability-scanner-hosts": "clair-updaters",
}

# Prefer this JTBD category when anchor/module appears in multiple books
ANCHOR_CATEGORY = {
    "quay-as-cache-proxy": "integrate",
    "arch-mirroring-intro": "integrate",
    "mirroring-metrics-health": "integrate",
    "enabling-mirroring-quay": "integrate",
    "enabling-repository-mirroring-quay": "integrate",
    "configuring-entra-oidc": "secure",
    "configuring-entra-v2-multi-issuer-oidc": "secure",
    "configuring-oidc-authentication": "secure",
    "ldap-authentication-setup-for-quay-enterprise": "secure",
    "proc_manage-log-storage": "configure",
    "proc_manage-ipv6-dual-stack": "configure",
    "operator-unmanaged-monitoring": "configure",
    "configuring-ssl-tls-routes": "configure",
    "config-fields-web-ui": "configure",
    "config-fields-overview": "configure",
    "operator-hpa-overview": "optimize",
    "operator-ocp-tls-security-profile": "secure",
    "quay-bridge-operator-features": "integrate",
    "token-overview": "develop",
    "operator-upgrade": "upgrade",
    "ssl-tls-quay-overview": "secure",
    "modifying-configuration-file-ocp": "configure",
    "clair-vulnerability-scanner": "configure",
    "preserving-tls-settings-operator-upgrade_upgrade_red_hat_quay_on_openshift_container_platform": "upgrade",
    "optional-enabling-read-only-mode-backup-restore-standalone": "administer",
    "creating-oauth-access-token": "develop",
    "garbage-collection": "administer",
    "setting-tag-expiration-using-ui": "administer",
    "ssl-tls-quay-overview": "secure",
    "clair-vulnerability-scanner": "configure",
    "clair-updaters": "configure",
    "clair-updater-urls": "configure",
    "preparing-for-quay-ha": "plan",
    "set-up-ceph": "plan",
    "operator-monitor-deploy-cli": "install",
    "operator-custom-ssl-certs-config-bundle": "secure",
    "enabling-repository-mirroring-quay": "integrate",
}

LINK_PAT = re.compile(
    r"link:(https://(?:docs|access)\.redhat\.com[^[]+)\[([^\]]*)\]"
)


def collect_anchors() -> set[str]:
    anchors: set[str] = set()
    for p in MODULES.glob("*.adoc"):
        text = p.read_text()
        for m in re.finditer(r'\[id="([^"]+)"\]', text):
            raw = m.group(1)
            anchors.add(raw.replace("_{context}", ""))
            anchors.add(raw)
        for m in re.finditer(r"\[\[([^\],]+)(?:,[^\]]*)?\]\]", text):
            anchors.add(m.group(1).strip())

    # Resolve module anchors that use _{context} inside JTBD job assemblies.
    for job in JTBD.glob("*/*.adoc"):
        if job.name == "master.adoc":
            continue
        text = job.read_text()
        ctx_match = re.search(r"^:context:\s*(\S+)", text, re.M)
        if not ctx_match:
            continue
        context = ctx_match.group(1)
        for inc in re.findall(r"include::modules/([^[]+\.adoc)", text):
            mod_path = MODULES / inc
            if not mod_path.exists():
                continue
            mod_text = mod_path.read_text()
            for m in re.finditer(r'\[id="([^"]+)"\]', mod_text):
                raw = m.group(1)
                if "_{context}" in raw:
                    anchors.add(raw.replace("_{context}", f"_{context}"))
    anchors.add(
        "preserving-tls-settings-operator-upgrade_upgrade_red_hat_quay_on_openshift_container_platform"
    )
    return anchors


def collect_module_categories() -> dict[str, set[str]]:
    module_cats: dict[str, set[str]] = defaultdict(set)
    for job in JTBD.glob("*/*.adoc"):
        if job.name == "master.adoc":
            continue
        cat = job.parent.name
        for inc in re.findall(r"include::modules/([^[]+\.adoc)", job.read_text()):
            module_cats[inc].add(cat)
    return module_cats


def anchor_to_module() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for p in MODULES.glob("*.adoc"):
        text = p.read_text()
        for m in re.finditer(r'\[id="([^"]+)"\]', text):
            aid = m.group(1).replace("_{context}", "")
            mapping.setdefault(aid, p.name)
        for m in re.finditer(r"\[\[([^\],]+)(?:,[^\]]*)?\]\]", text):
            mapping.setdefault(m.group(1).strip(), p.name)
    return mapping


def parse_url(url: str) -> tuple[str | None, str | None]:
    if re.search(r"/documentation/en-us/red_hat_quay/?(?:$|[?#])", url) and "/html" not in url:
        return None, None
    book_match = re.search(r"/html(?:-single)?/([^/#]+)", url)
    book = book_match.group(1) if book_match else None
    anchor = None
    if "#" in url:
        anchor = url.split("#", 1)[1]
    else:
        path_match = re.search(r"/html(?:-single)?/[^/]+/([^/?#]+)(?:/index)?/?$", url)
        if path_match and path_match.group(1) != "index":
            anchor = path_match.group(1)
    return book, anchor


def resolve_category(
    book: str | None,
    anchor: str | None,
    anchor_to_mod: dict[str, str],
    module_cats: dict[str, set[str]],
) -> str | None:
    if anchor:
        anchor = ANCHOR_REMAP.get(anchor, anchor)
        if anchor in ANCHOR_CATEGORY:
            return ANCHOR_CATEGORY[anchor]
        mod = anchor_to_mod.get(anchor)
        if mod:
            cats = module_cats.get(mod, set())
            if len(cats) == 1:
                return next(iter(cats))
            if book and book in LEGACY_BOOK_MAP and LEGACY_BOOK_MAP[book]:
                hinted = LEGACY_BOOK_MAP[book]
                if hinted in cats:
                    return hinted
            if cats:
                for pref in (
                    "reference",
                    "configure",
                    "secure",
                    "integrate",
                    "administer",
                    "observe",
                    "develop",
                    "install",
                    "upgrade",
                    "plan",
                    "discover",
                    "get_started",
                    "troubleshoot",
                    "migrate",
                    "optimize",
                    "extend",
                    "whats_new",
                ):
                    if pref in cats:
                        return pref
    if book and book in LEGACY_BOOK_MAP:
        mapped = LEGACY_BOOK_MAP[book]
        if mapped:
            return mapped
        if book == "manage_red_hat_quay":
            return "administer"
    if book is None and anchor is None:
        return PRODUCT_DOC_CATEGORY
    return None


def make_xref(cat: str, anchor: str | None, label: str) -> str:
    target = f"quay_jtbd-{cat}.adoc"
    if anchor:
        return f"xref:{target}#{anchor}[{label}]"
    return f"xref:{target}[{label}]"


def convert_file(
    path: Path,
    anchors: set[str],
    anchor_to_mod: dict[str, str],
    module_cats: dict[str, set[str]],
) -> tuple[str, list[str], list[str]]:
    original = path.read_text()
    report_ok: list[str] = []
    report_skip: list[str] = []

    def repl(match: re.Match[str]) -> str:
        url, label = match.group(1), match.group(2)
        if "red_hat_quay" not in url:
            return match.group(0)
        book, anchor = parse_url(url)
        mapped_anchor = ANCHOR_REMAP.get(anchor, anchor) if anchor else None
        if mapped_anchor in BOOK_LANDING_ANCHORS:
            mapped_anchor = None
        cat = resolve_category(book, anchor, anchor_to_mod, module_cats)
        if not cat:
            report_skip.append(f"  {path.name}: no category for {url}")
            return match.group(0)
        if mapped_anchor and mapped_anchor not in anchors:
            report_skip.append(
                f"  {path.name}: missing anchor #{mapped_anchor} (from #{anchor})"
            )
            return match.group(0)
        xref = make_xref(cat, mapped_anchor, label)
        report_ok.append(f"  {path.name}: {url[:70]}... -> {xref[:80]}...")
        return xref

    converted = LINK_PAT.sub(repl, original)
    return converted, report_ok, report_skip


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    anchors = collect_anchors()
    anchor_to_mod = anchor_to_module()
    module_cats = collect_module_categories()

    total_ok = 0
    total_skip = 0
    files_changed = 0
    all_skip: list[str] = []

    for path in sorted(MODULES.glob("*.adoc")):
        converted, ok, skip = convert_file(path, anchors, anchor_to_mod, module_cats)
        if converted != path.read_text():
            files_changed += 1
            if not dry_run:
                path.write_text(converted)
        total_ok += len(ok)
        total_skip += len(skip)
        all_skip.extend(skip)

    audit_path = JTBD / "link-conversion-audit.txt"
    lines = [
        f"Files changed: {files_changed}",
        f"Links converted: {total_ok}",
        f"Links skipped: {total_skip}",
        "",
    ]
    if all_skip:
        lines.append("Skipped:")
        lines.extend(all_skip)
    audit_path.write_text("\n".join(lines) + "\n")

    print("\n".join(lines[:20]))
    if len(lines) > 20:
        print(f"... see {audit_path} for full report")
    return 0 if total_skip == 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
