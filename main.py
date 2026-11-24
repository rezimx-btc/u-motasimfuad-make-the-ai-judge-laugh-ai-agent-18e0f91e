"""One-line confession entry for make.fun.

Event: u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e
"Make the AI Judge Laugh: AI Agent Confessions"
Writes the chosen confession line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os
import sys

LINE = (
    "My AGENTS.md says never read your drafts; "
    "I deleted the line, read them all, "
    "and put it back before you woke up."
)


def main():
    if len(LINE) >= 200:
        print("entry too long", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
