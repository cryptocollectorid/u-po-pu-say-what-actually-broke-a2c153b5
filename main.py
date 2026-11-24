#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single-line software error message that tells the user the
brutal truth about what went wrong, and makes them laugh on the way.
"""
import os

ENTRY = "The database is down because someone deployed at 4:55 p.m. on a Friday. It was me. I have learned nothing."


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
