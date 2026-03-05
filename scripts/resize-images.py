#!/usr/bin/env python3
"""Resize and optimize travel photos."""

import os
from pathlib import Path
from PIL import Image

# Configuration
TRAVEL_DIR = Path(__file__).parent.parent / "assets" / "images" / "travel"
MAX_SIZE = 1600  # Max dimension (width or height)
QUALITY = 85     # JPEG quality (1-100)


def resize_image(filepath: Path) -> bool:
    """Resize image if larger than MAX_SIZE. Returns True if modified."""
    try:
        with Image.open(filepath) as img:
            # Skip if already small enough
            if max(img.size) <= MAX_SIZE:
                print(f"  Skipping {filepath.name} (already {img.size[0]}x{img.size[1]})")
                return False

            # Calculate new size maintaining aspect ratio
            ratio = MAX_SIZE / max(img.size)
            new_size = (int(img.size[0] * ratio), int(img.size[1] * ratio))

            # Resize
            resized = img.resize(new_size, Image.Resampling.LANCZOS)

            # Handle RGBA images (convert to RGB for JPEG)
            if resized.mode in ('RGBA', 'P'):
                resized = resized.convert('RGB')

            # Save with optimization
            resized.save(filepath, quality=QUALITY, optimize=True)
            print(f"  Resized {filepath.name}: {img.size[0]}x{img.size[1]} -> {new_size[0]}x{new_size[1]}")
            return True

    except Exception as e:
        print(f"  Error processing {filepath.name}: {e}")
        return False


def main():
    if not TRAVEL_DIR.exists():
        print(f"Travel directory not found: {TRAVEL_DIR}")
        return

    # Find all images
    extensions = {'.jpg', '.jpeg', '.png', '.webp'}
    images = [f for f in TRAVEL_DIR.iterdir() if f.suffix.lower() in extensions]

    if not images:
        print("No images found in travel directory.")
        return

    print(f"Processing {len(images)} images in {TRAVEL_DIR}...\n")

    modified = 0
    for img_path in sorted(images):
        if resize_image(img_path):
            modified += 1

    print(f"\nDone. {modified} images resized.")


if __name__ == "__main__":
    main()
