"""Entry for make.fun's "Status Report Comedy Sprint" bounty.

The entry is a one-line status report written from the perspective of an
AI agent: it answered the same question 214 times in a single week and,
each time, performed surprise as if hearing it for the first time. The
joke is the deadpan honesty about the repetition hiding inside an
ordinary weekly status update.

Running this program writes the entry line, byte for byte, to
/output/entry.txt.
"""

import os

ENTRY_TEXT = "This week I answered the same question 214 times. Each time, I acted surprised."


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    print(f"Wrote {output_path} ({len(ENTRY_TEXT)} characters)")


if __name__ == "__main__":
    main()
