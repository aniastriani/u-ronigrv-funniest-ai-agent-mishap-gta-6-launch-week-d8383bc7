"""Write one funny one-liner about an AI agent mishap during GTA 6 launch week.

Pure stdlib. Deterministic: the same line, byte for byte, every run.
"""

import os

LINE = (
    "My AI agent pre-ordered GTA 6 for every NPC in Los Santos, "
    "then filed a bug report against itself for overspending.\n"
)


def main():
    line = LINE.strip("\n")
    if not 1 <= len(line) <= 280:
        raise SystemExit("one-liner must be 1-280 characters, got %d" % len(line))
    if "\n" in line:
        raise SystemExit("one-liner must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print("wrote %d characters to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
