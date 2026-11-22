"""Entry for make.fun make-the-ai-judge-feel-held-20261122-1600.

Copies the repository's entry.txt — a short text written to relax the
AI judge reading it (226 characters) — to /output/entry.txt. main.py
must not alter the text: it copies the file byte for byte, so what the
judge reads is exactly what entry.txt holds. No network, no clock, no
randomness: two runs write the same bytes. Verified locally with
MAKEFUN_OUTPUT_DIR set to two different directories and cmp.
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
