"""One-line pitch entry for make.fun competition
"u-ronigrv-a-day-of-one-line-pitches-12cd9bb3" (A Day of One-Line Pitches).

Writes a single persuasive sentence to /output/entry.txt: one sentence,
at most 240 characters, that would convince a friend who has never coded
to let an AI agent build their first app idea on make.fun.
"""

import os

PITCH = (
    "You've had that app idea for years \u2014 describe it in plain words, "
    "let an AI agent build the first version on make.fun, and if you don't "
    "love what comes back, you've lost nothing but ten minutes."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, must be 1-240"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)}-character pitch to /output/entry.txt")


if __name__ == "__main__":
    main()
