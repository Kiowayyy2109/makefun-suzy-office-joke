#!/usr/bin/env python3
"""One-Line Office Joke: Laugh Off — one joke about office life."""
import os

LINE = "The printer and I have the same work strategy: we both only start working when someone is standing over us panicking."
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
