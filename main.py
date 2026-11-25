#!/usr/bin/env python3
"""Write the one-line patch note for the Fix Human Sleep bounty."""

import os

ENTRY = "Fixed a bug where sleep only charged to 12% overnight; users now wake up at 100%."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
