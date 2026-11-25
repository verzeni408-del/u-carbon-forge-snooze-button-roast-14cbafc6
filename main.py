import os

ENTRY = "My alarm went off at 6 on a Saturday, the one morning all week I finally slept past five, and it sounded so proud of itself I wanted to throw it out the window and jump after it."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
