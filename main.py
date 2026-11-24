"""Worst AI Advice — a one-line entry for the make.fun 48-hour tight line open.

The job of this script is deliberately tiny: it drops a single line of
spectacularly bad guidance into the file the competition reads. The line
itself is the whole entry — no extra formatting, no trailing newline, so
the file holds exactly the characters the judges score.
"""

from pathlib import Path

ENTRY = "For best results, water your laptop weekly. Hydration improves performance in all systems."

# The competition only accepts a short single line, so refuse to ship
# anything outside that band instead of silently writing it.
assert 1 <= len(ENTRY) <= 140, "entry must be between 1 and 140 characters"


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    # Write as plain UTF-8 with no newline appended: the gate measures the
    # raw bytes, so every byte present must belong to the line itself.
    # Keeping the write unconditional also keeps the script trivially
    # re-runnable — a second run produces the identical file.
    target.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
