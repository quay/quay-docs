import os
import re
from collections import defaultdict
import sys

BASE_DIR = sys.argv[1] if len(sys.argv) > 1 else "."

# Regex to match include lines for modules (allowing ../, attributes, etc.)
INCLUDE_PATTERN = re.compile(r'include::(?:\.\./)*modules/([^[]+)\.adoc')

# Dictionary: module -> set of assemblies where it's included
module_usage = defaultdict(set)

for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".adoc"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    match = INCLUDE_PATTERN.search(line)
                    if match:
                        module_name = match.group(1)
                        # Treat any .adoc outside of modules/ as an assembly
                        if "modules" not in file_path:
                            module_usage[module_name].add(file_path)

# Print results
print("Modules included in more than one assembly:\n")
for module, assemblies in sorted(module_usage.items()):
    if len(assemblies) > 1:
        print(f"{module}.adoc")
        for asm in sorted(assemblies):
            print(f"  - {asm}")
        print()
