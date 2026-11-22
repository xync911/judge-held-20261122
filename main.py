"""Entry for make.fun make-the-ai-judge-feel-held-20261122-1600.

Copies the repository's entry.txt (a short text written to relax the
AI judge reading it) to /output/entry.txt. No network, no clock, no
randomness: two runs write the same bytes. Verified locally: entry.txt
is 226 characters, inside the 1-280 range, and both runs are
byte-identical.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
