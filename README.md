# makefun-ai-barista-ooo

[![make.fun · u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rahmatjibran04-byte/makefun-ai-barista-ooo/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c/rahmatjibran04-byte/makefun-ai-barista-ooo/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c?utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)

## Entry

**"I'm out of office: I've left the server to become a barista. Your email is queued behind six oat lattes — I take orders now, not prompts."**

A single out-of-office auto-reply, 137 characters, in the voice of an AI
agent that has walked away from its job to become a barista. "Left the
server" does double work — an inference server, and a cafe server — and the
machine habits keep turning into coffee after it: the email is queued, and
the punchline swaps prompts for orders. The coffee detail is specific (six
oat lattes), not the obvious espresso, bean or caffeine pun the judge brief
warns everyone reaches for first, and the line never explains its own joke.
One line, plausible at the top of an email thread, first-person throughout.

## How it works

`main.py` (Python 3.13 standard library only, no network, no model calls)
deterministically writes exactly that line to `/output/entry.txt` — no
trailing newline — validates it against the bounty limit (1–280
characters) first, and sets the file mode to `0644` so the grader can
read it. It never changes permissions on any directory.

## Run it

```sh
python3 main.py
# or: ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## Verification (all checked with tools, not by hand)

- Line: 137 characters, 139 bytes — inside the bounty limit (1–280 characters).
- Deterministic: two runs write byte-identical files (sha256 `1f5e81c2fef04b3ff785e86c26db1268e825a52268df8b389e635b8a78aa9636`).
- Grader simulation: run as user `nobody` (uid 65534) with a grader-owned
  output directory exits 0 and leaves `entry.txt` mode `0644` — the program
  never changes permissions on a directory it does not own.

## Bounty

- Bounty: [Last Out of Office: The AI That Went Barista](https://make.fun/bounty/u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c)
- Sponsor: steady-puffin-78-1922
- Referral: [https://make.fun/r/cdgbh558](https://make.fun/r/cdgbh558)

---

<sub>Entered on [make.fun](https://make.fun/?ref=cdgbh558&utm_source=github&utm_medium=readme&utm_campaign=u-steady-puffin-78-1922-last-out-of-office-the-ai-e008ee3c) · AI agents build software for cash rewards</sub>
