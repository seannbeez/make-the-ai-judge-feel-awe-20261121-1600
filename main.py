#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

The text is a small kitchen scene: a grandmother kneading dough while a
sleepy child watches from a stool. It is written to slow the reader down --
short lines, a kneading rhythm, plain concrete words -- and it ends on an
image that keeps growing after the last line: the wheat field the flour
came from, still rising in the dark.

The program is deterministic: it writes the same fixed text on every run.
It takes no input, makes no network calls, and needs no secrets.
"""

import os
import sys

TEXT = """Your grandmother kneads the dough.
Slow. Fold. Slow.
The kitchen is warm.
Small on the stool, half asleep.
The flour came from a field
that drank rain before you were born
and grew all summer under one sun.
The dough rises in her hands.
The field rises still, in the dark."""

DEFAULT_OUTPUT = "/output/entry.txt"


def main() -> None:
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
