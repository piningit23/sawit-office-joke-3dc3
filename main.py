#!/usr/bin/env python3
"""Office joke entry for make.fun's 'The Funniest Office Joke, Judged Head to Head'.

Writes a single line of office comedy (1-200 characters) to /output/entry.txt.
The joke is written by hand, deterministic, stdlib only, no network, no input.
"""

JOKE = (
    "I replied-all asking everyone to stop replying-all, and now "
    "my inbox has 47 apologies, one resignation, and a calendar "
    "invite to discuss it."
)
# Structure: setup (a reply-all plea) -> escalation (47 apologies, a
# resignation) -> punchline last (a calendar invite to discuss it),
# turning on the reply-all chain everyone in an office recognises.

import os


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Verify the round-trip: what the judge reads must be exactly the joke.
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == text
    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
