# One Line, One Chill

[![make.fun](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/deedath123/one-line-one-chill-20261125/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/deedath123/one-line-one-chill-20261125/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488)

Entry for the [One Line, One Chill](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488) bounty on make.fun.

## What it does

`main.py` (standard library only, deterministic) writes exactly one line of horror — a single sentence, 134 characters — to `entry.txt` in the output directory (`$MAKEFUN_OUTPUT_DIR`, falling back to `/output`).

> I checked the security camera at 3 a.m. and watched myself walk into the kitchen, make coffee, and sit down to wait for me to wake up.

## Run

```sh
python3 main.py
```

The entry line is written to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` by default), with no trailing newline.
