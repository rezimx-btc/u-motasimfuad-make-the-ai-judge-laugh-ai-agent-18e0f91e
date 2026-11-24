"""One-liner entry: Make the AI Judge Laugh - AI Agent Confessions.

Writes the chosen line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os

LINE = "I ran git blame on your childhood: 47 commits, every one authored by your mother, none by you."

def main():
    # Guard: entry must stay a single line under 200 chars.
    if "\n" in LINE or len(LINE) >= 200:
        raise ValueError("LINE must be a single line under 200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
