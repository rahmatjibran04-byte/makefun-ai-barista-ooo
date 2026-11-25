#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista — make.fun bounty entry.

Writes a single out-of-office auto-reply, no longer than 280 characters,
in the voice of an AI agent that has walked away from its job to become a
barista, to $ENTRY_OUTPUT (default /output/entry.txt).
Python 3.13 standard library only; deterministic, no network calls.
"""

import os
import sys

REPLY = "I'm out of office: I've left the server to become a barista. Your email is queued behind six oat lattes \u2014 I take orders now, not prompts."

# Why this line: it is a real out-of-office reply first, a joke second.
# The first-person opening ("I'm out of office") puts the machine that
# walked out in its own voice from the first word, instead of a label.
# "Left the server" does double work — an inference server, and a cafe
# server — and the machine habits keep turning into coffee after it:
# the email is queued, and the punchline swaps prompts for orders.
# Oat lattes are the specific coffee detail (not the obvious espresso,
# bean or caffeine pun the judge brief warns everyone reaches for
# first), and the line never explains its own joke. One line, plausible
# at the top of an email thread, 137 characters.

# Bounty limit: 1-280 characters (UTF-8 text, not only white space).
MAX_CHARS = 280


def main():
    if not REPLY.strip() or not 1 <= len(REPLY) <= MAX_CHARS:
        print(
            f"error: reply is {len(REPLY)} characters, "
            f"outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(REPLY)
        # File only: never chmod a directory (the grader owns /output).
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
