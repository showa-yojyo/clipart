#!/usr/bin/env python

"""pattern.py: An example like <Rolling an image> in Pillow document.

usage:
  pattern.py --help
  pattern.py FILE
"""

from argparse import (ArgumentParser, FileType)
import sys
from PIL import Image

def parse_args(args):
    """Return the command line arguments."""

    parser = ArgumentParser()
    parser.add_argument(
        'file',
        type=FileType('rb'),
        help='a PNG file')

    return parser.parse_args(args=args or ('--help',))

def main(args=sys.argv[1:]):
    sys.exit(run(parse_args(args)))

def run(args):
    """Create a wallpaper image from a PNG file."""

    src = Image.open(args.file)
    target = swap_quadrants(src)
    paste_with_alpha(target, src, (0, 0), 0x10)
    target.show()

    answer = input('Save this? ([y]/n) :')
    if answer.lower() == 'n':
        return

    path = input('pattern.py: Input file name to save ')
    target.save(path)

def swap_quadrants(img):
    """Quarter the image and swap two diagonal quadrant pairs."""

    boxes = quarter_bbox(img)
    regions = tuple(img.crop(box) for box in boxes)

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
