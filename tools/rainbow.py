#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""rainbow.py

Usage:
  rainbow.py
"""

from colorsys import hsv_to_rgb

__version__ = '0.0.0'

stop_template = '''\
      <stop
         id="stop-rainbow-{id:02d}"
         offset="{offset}"
         style="stop-color:#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x};stop-opacity:1" />'''

def main():
    s, v = 1.0, 1.0
    num_div = 16
    kwargs = {}

    for i in range(num_div):
        offset = 1.0 * i / num_div
        kwargs['offset'] = offset
        kwargs['id'] = i
        kwargs['rgb'] = [round(j * 0xFF) for j in hsv_to_rgb(offset, s, v)]
        print(stop_template.format(**kwargs))

    kwargs['offset'] = 1
    kwargs['id'] = num_div
    r, g, b = (round(j * 0xFF) for j in hsv_to_rgb(1.0, s, v))
    kwargs['r'] = r
    kwargs['g'] = g
    kwargs['b'] = b
    print(stop_template.format(**kwargs))

if __name__ == '__main__':
    main()
