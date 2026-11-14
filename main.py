"""Make the AI judge happy — entry program.

Copies the bundled image to /output/entry.png: a golden retriever puppy
leaping in mid-air to catch a bright red maple leaf, mouth open in a big
happy grin, warm golden-hour autumn light. Deterministic: the same bytes
on every run. Standard library only, no network.
"""

import hashlib
import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.png"


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    # Fail loudly on a truncated copy instead of submitting a broken image.
    if _sha256(SOURCE) != _sha256(OUTPUT):
        raise SystemExit("entry.png copy mismatch")


if __name__ == "__main__":
    main()
