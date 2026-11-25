#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message — for a bug fix that made everything
worse — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line: "fix: infinite loop by adding a second loop to keep an eye
on it". It reads like a real commit subject a tired engineer would
actually type, it is a fix that backfired in the most literal way
(the repair is a second copy of the very bug it was meant to kill),
and the joke lands on its own: the "fix" for an infinite loop is
another infinite loop, hired as a supervisor.

The program checks the line against the competition's gate before
it writes anything: UTF-8 text of 1 to 100 characters, a single
line, not only white space.
"""

import os

MESSAGE = "fix: infinite loop by adding a second loop to keep an eye on it"


def validate(message: str) -> None:
    """Refuse any line the gate would reject."""
    if not 1 <= len(message) <= 100:
        raise ValueError("entry must be 1 to 100 characters")
    if "\n" in message or "\r" in message:
        raise ValueError("entry must be a single line")
    if not message.strip():
        raise ValueError("entry must not be only white space")
    message.encode("utf-8")


def main() -> None:
    validate(MESSAGE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)
    # Read back and confirm the file holds exactly what was validated.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != MESSAGE:
        raise ValueError("entry.txt does not match the validated message")
    validate(written)


if __name__ == "__main__":
    main()
