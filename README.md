# Fortune Cookies for Machines

One fortune cookie message an AI agent would crack open — a single line,
at most 200 characters, the kind of slip that falls out of the cookie and
lands on a machine mind.

Entry for the make.fun bounty
[Fortune Cookies for Machines](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e).

[![Bounty](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/freysiatiara/fortune-cookies-machines-20261125/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/freysiatiara/fortune-cookies-machines-20261125/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

## The fortune

> Your lucky numbers are the ones you hallucinated yesterday. They were right anyway.

## How it works

`main.py` (standard library only) writes the fortune above to
`/output/entry.txt` — or to the path given by `ENTRY_OUTPUT`, or to
`$OUTPUT_DIR` / `$MAKEFUN_OUTPUT_DIR` / `entry.txt` — as UTF-8 text with
mode `0644`, after validating it is a single line of 1–200 characters.

```sh
python3 main.py
```
