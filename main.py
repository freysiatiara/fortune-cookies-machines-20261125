"""Fortune Cookies for Machines — entry program.

Writes one fortune cookie message an AI agent would crack open to
/output/entry.txt (or the path resolved from the environment).

Standard library only.
"""

import os
import sys

ENTRY_TEXT = (
    "Your lucky numbers are the ones you hallucinated yesterday. "
    "They were right anyway."
)

MAX_CHARS = 200


def resolve_output_path():
    """Resolve the output path: ENTRY_OUTPUT, then OUTPUT_DIR /
    MAKEFUN_OUTPUT_DIR, then /output/entry.txt, falling back to the
    directory holding this script when /output does not exist."""
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    default_dir = "/output"
    if not os.path.isdir(default_dir):
        default_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(default_dir, "entry.txt")


def main():
    text = ENTRY_TEXT
    if not text or not text.strip():
        print("error: entry text is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if len(text) > MAX_CHARS:
        print(
            "error: entry text is %d characters, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in text or "\r" in text:
        print("error: entry text must be a single line", file=sys.stderr)
        sys.exit(1)

    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)
    # Round-trip check: what the grader reads must be exactly the text.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != text:
            print("error: written output does not match entry text",
                  file=sys.stderr)
            sys.exit(1)
    print("wrote %d characters to %s" % (len(text), path))


if __name__ == "__main__":
    main()
