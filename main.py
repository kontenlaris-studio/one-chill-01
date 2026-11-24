"""One Line, One Chill entry: a phone resting in a drawer, owner included."""

import os

JOKE = (
    "I put my phone in a drawer, and the drawer did not light up, buzz, or "
    "have opinions. We are both recharging."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
