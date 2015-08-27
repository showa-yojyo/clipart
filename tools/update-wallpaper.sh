#!/bin/bash
# update-wallpaper.sh: Overwrite wallpaper.bmp under mattari09 directory.
#
# To execute this shell script, the following packages are required:
#
# - Inkscape
# - ImageMagick
#
# To test this script, follow the next instructions:
#
# 1. Edit and save `mattari-wallpaper.svg` (with Inkscape).
# 2. Make sure that all paths (e.g. LOCAL_ROOT) defined in this script
#    are correct.
# 3. Run this script.
# 4. Execute `まったり麻雀.exe` and start a game to see if the wallpaper
#    is the same as you saved in 1.
#
# Note that this script is just for me (@showa_yojyo).

# Windows style path
LOCAL_ROOT="D:\home\yojyo\devel\sketchbook"
MATTARI_ROOT="D:\Program Files\mattari09"
SOURCE_SVG="$LOCAL_ROOT\svg\mattari-wallpaper.svg"
DEST_BMP="$MATTARI_ROOT\wallpaper.bmp"

# Cygwin style path
INKSCAPE='/cygdrive/d/Program Files/inkscape-0.48.5/inkscape-0.48.5.exe'

# Invoke Inkscape to generate a PNG file from the SVG file.
DEST_PNG="$(cygpath -aw $(mktemp --suffix=.png))"
"$INKSCAPE" --file="$SOURCE_SVG" --export-area-page --export-png="$DEST_PNG"

# XXX
sleep 3s

# Convert PNG to BMP by using ImageMagick's converter tool.
convert "$DEST_PNG" bmp3:"$DEST_BMP"

# Clean up.
rm -f "$DEST_PNG"
