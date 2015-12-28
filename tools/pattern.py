#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pattern.py: An example like <Rolling an image> in Pillow document.

usage:
  pattern.py --help
  pattern.py FILE
"""

from argparse import ArgumentParser, FileType
from PIL import Image

def configure():
    """Create an object of class ArgumentParser."""

    parser = ArgumentParser()
    parser.add_argument(
        'file',
        type=FileType('rb'),
        help='a PNG file')

    return parser

def main():
    """Create a wallpaper image from a PNG file."""

    args = configure().parse_args()

    src = Image.open(args.file)
    target = swap_quadrants(src)
    paste_with_alpha(target, src, (0, 0), 0x10)

    answer = input('pattern.py: Save this? [y/n] ')
    if answer.lower() != 'y':
        return

    path = input('pattern.py: Input file name to save ')
    target.save(path)

def swap_quadrants(img):
    """Quarter the image and swap two diagonal quadrant pairs."""

    boxes = quarter_bbox(img)
    regions = [img.crop(box) for box in boxes]

    target = img.copy()
    paste_with_alpha(target, regions[3], (0, 0), 0x80)
    paste_with_alpha(target, regions[2], (regions[3].size[0], 0), 0x80)
    paste_with_alpha(target, regions[1], (0, regions[3].size[1]), 0x80)
    paste_with_alpha(target, regions[0], regions[3].size, 0x80)

    return target

def paste_with_alpha(target, source, left_upper, opacity):
    """An alpha_composite-like operation."""

    mask = Image.new('L', source.size, opacity)
    target.paste(source, left_upper, mask=mask)

def quarter_bbox(img):
    """Quarter the bounding box of an image."""

    sx, sy = img.size
    xmid, ymid = sx // 2, sy // 2

    return [
        (0, 0, xmid, ymid),
        (xmid, 0, sx, ymid),
        (0, ymid, xmid, sy),
        (xmid, ymid, sx, sy),]

if __name__ == '__main__':
    main()
