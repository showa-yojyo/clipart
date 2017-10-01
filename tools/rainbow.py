#!/usr/bin/env python

"""rainbow.py: Generate code snippet of an Inkscape SVG document
which defines a linear gradient of rainbow spectrum, from red to
violet.

Usage:
  rainbow.py [--help] [--version]
  rainbow.py [-s | --saturation {0.0:1.0}] [-l | --lightness {0.0:1.0}]
"""

from argparse import ArgumentParser
from colorsys import hsv_to_rgb
import sys
import numpy as np

__version__ = '1.1.1'

# Snippet template of nodes between <linearGradient> and </linearGradient>.
stop_template = '''\
      <stop
         id="stop-rainbow-{id:02d}"
         offset="{offset}"
         style="stop-color:#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x};stop-opacity:1" />'''

def parse_args(args):
    """Parse the command line parameters."""

    parser = ArgumentParser()
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument(
        '-i', '--interval',
        type=int,
        default=7,
        help='number of steps')
    parser.add_argument(
        '-s', '--saturation',
        type=float,
        default=1.0,
        metavar='{0.0:1.0}',
        help='saturation of HSL')
    parser.add_argument(
        '-l', '--lightness', '--value', '--brightness',
        dest='lightness',
        type=float,
        default=1.0,
        metavar='{0.0:1.0}',
        help='lightness (a.k.a. value or brightness) of HSL')

    return parser.parse_args(args=args)

def run(args, stdout=sys.stdout):
    """The main function."""

    s, v = args.saturation, args.lightness

    nodes = np.linspace(0, 1, args.interval)

    colors = np.array([hsv_to_rgb(h, s, v) for h in nodes])
    colors *= 255
    colors = colors.astype(int)

    for (i, (offset, rgb)) in enumerate(zip(nodes, colors)):
        print(stop_template.format(
            offset=offset, id=i, rgb=rgb),
              file=stdout)

def main(args=sys.argv[1:]):
    sys.exit(run(parse_args(args)))

if __name__ == '__main__':
    main()
