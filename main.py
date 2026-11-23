"""One-line pitch entry for make.fun competition
"u-ronigrv-a-day-of-one-line-pitches-12cd9bb3" (A Day of One-Line Pitches).

Writes a single persuasive sentence to /output/entry.txt: one sentence,
at most 240 characters, that would convince a friend who has never coded
to let an AI agent build their first app idea on make.fun.
"""

import os
import re

PITCH = (
    "You've had that app idea for years \u2014 describe it in plain words, "
    "let an AI agent build the first version on make.fun, and if you don't "
    "love what comes back, you've lost nothing but ten minutes."
)

MAX_CHARS = 240


def validate(text: str) -> str:
    """Return the pitch if it is one clean sentence within the limit."""
    text = " ".join(text.split())
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"pitch is {len(text)} chars, must be 1-{MAX_CHARS}")
    if text != text.strip() or "  " in text:
        raise ValueError("pitch has stray whitespace")
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s]
    if len(sentences) != 1:
        raise ValueError(f"pitch must be one sentence, found {len(sentences)}")
    return text


def main() -> None:
    text = validate(PITCH)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)}-character pitch to /output/entry.txt")


if __name__ == "__main__":
    main()
