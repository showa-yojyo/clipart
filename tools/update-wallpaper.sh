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

if [ -z "$1" ]; then
    echo "Usage: `basename $0` current_version"
    exit 1
fi

# Current version of まったり麻雀
#VERSION=${1-'0.9.12'}
VERSION=${1}

# Windows style path
LOCAL_ROOT="D:\home\yojyo\devel\sketchbook"
MATTARI_ROOT="D:\Program Files\mattari09"
SOURCE_SVG="$LOCAL_ROOT\svg\mattari-wallpaper.svg"
DEST_BMP="$MATTARI_ROOT\wallpaper.bmp"

# Cygwin style path
INKSCAPE='/cygdrive/d/Program Files/Inkscape/inkscape.exe'

WORKING_SVG="$(cygpath -aw $(mktemp --suffix=.svg))"
sed -e "s/{{ VERSION }}/$VERSION/g" "$SOURCE_SVG" > "$WORKING_SVG"

# Invoke Inkscape to generate a PNG file from the SVG file.
DEST_PNG="$(cygpath -aw $(mktemp --suffix=.png))"
"$INKSCAPE" --file="$WORKING_SVG" --export-area-page --export-png="$DEST_PNG"

# XXX
sleep 3s

# Convert PNG to BMP by using ImageMagick's converter tool.
convert "$DEST_PNG" bmp3:"$DEST_BMP"

# Clean up.
rm -f "$WORKING_SVG" "$DEST_PNG"
