#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys

try:
    import yaml
    from PIL import Image
except ImportError:
    raise SystemExit("PyYAML and Pillow are required: python -m pip install PyYAML Pillow")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--spec", required=True)
    parser.add_argument("--images-dir", required=True)
    parser.add_argument("--ratio-tolerance", type=float, default=0.01)
    args = parser.parse_args()
    spec = yaml.safe_load(Path(args.spec).read_text(encoding="utf-8"))
    folder = Path(args.images_dir)
    errors = []

    for slide in spec.get("slides", []):
        expected = Path(slide["output"]).name
        path = folder / expected
        if not path.exists():
            errors.append(f"missing {expected}")
            continue
        with Image.open(path) as image:
            ratio = image.width / image.height
            if abs(ratio - 16 / 9) > args.ratio_tolerance:
                errors.append(f"{expected}: ratio {ratio:.4f} is not 16:9")
            print(f"{expected}: {image.width}x{image.height} ratio={ratio:.4f}")

    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID: all expected images exist and match the target ratio")
    return 0


if __name__ == "__main__":
    sys.exit(main())

