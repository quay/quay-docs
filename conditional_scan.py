import os
import re
from collections import defaultdict
import sys

BASE_DIR = sys.argv[1] if len(sys.argv) > 1 else "."

# Regex patterns for conditionals
IFDEF_PATTERN = re.compile(r'^\s*(ifdef::|endif::)')
IFEVAL_PATTERN = re.compile(r'^\s*(ifeval::|endif::)')

# Track which files use conditionals
files_with_conditionals = defaultdict(set)

for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".adoc"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if IFDEF_PATTERN.search(line):
                        files_with_conditionals[file_path].add("ifdef/endif")
                    if IFEVAL_PATTERN.search(line):
                        files_with_conditionals[file_path].add("ifeval/endif")

# Print results
print("Files using AsciiDoc conditionals:\n")
for filepath, types in sorted(files_with_conditionals.items()):
    print(f"{filepath}")
    for t in sorted(types):
        print(f"  - {t}")
    print()
