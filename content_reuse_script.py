import os
import re
import sys
from collections import defaultdict

BASE_DIR = sys.argv[1] if len(sys.argv) > 1 else "."

# Regex for [NOTE] lines
NOTE_START_PATTERN = re.compile(r'^\[NOTE\]')
NOTE_END_PATTERN = re.compile(r'^$')  # Assume NOTE block ends at first blank line

# Map note text -> set of files that contain it
note_occurrences = defaultdict(set)

for root, _, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith(".adoc"):
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                i = 0
                while i < len(lines):
                    line = lines[i].strip()
                    if NOTE_START_PATTERN.match(line):
                        note_lines = []
                        i += 1
                        # Capture all subsequent lines until blank or end of file
                        while i < len(lines) and lines[i].strip() != "":
                            note_lines.append(lines[i].strip())
                            i += 1
                        note_text = " ".join(note_lines)
                        if note_text:  # skip empty notes
                            note_occurrences[note_text].add(file_path)
                    else:
                        i += 1

# Print notes that appear in more than one file
print("Recurring NOTE blocks:")
for note_text, files in note_occurrences.items():
    if len(files) > 1:
        print(f"\nNOTE: {note_text}")
        for f in sorted(files):
            print(f"  - {f}")
