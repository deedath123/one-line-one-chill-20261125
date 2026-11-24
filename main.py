"""One Line, One Chill — make.fun entry.

Writes exactly one line of horror (a single sentence) to entry.txt.
Standard library only, fully deterministic.
"""

import os

LINE = (
    "I checked the security camera at 3 a.m. and watched myself walk "
    "into the kitchen, make coffee, and sit down to wait for me to wake up."
)


def main() -> None:
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
