from __future__ import division
from __future__ import print_function
import sys


def get_decimal_length(value):
    assert value>=0
    digits = 0
    while True:
        value //= 10
        digits += 1
        if value == 0:
            break
    return digits


def rgb_to_hsv(rgb_vals):

    rgb_vals = [x / 255.0 for x in rgb_vals]
    max_pixel_val = max(rgb_vals)
    min_pixel_val = min(rgb_vals)
    delta_pixel_val = max_pixel_val - min_pixel_val

    # if all the values are equal, the color is in the scale of gray
    if delta_pixel_val == 0:
        return [0, 0, min_pixel_val]

    # max == R
    hue = 0
    if max_pixel_val == rgb_vals[0]:
        hue = 60 * (((rgb_vals[1] - rgb_vals[2]) / delta_pixel_val) % 6.0)
    # max == G
    elif max_pixel_val == rgb_vals[1]:
        hue = 60 * (((rgb_vals[2] - rgb_vals[0]) / delta_pixel_val) + 2)
    # max == B
    elif max_pixel_val == rgb_vals[2]:
        hue = 60 * (((rgb_vals[0] - rgb_vals[1]) / delta_pixel_val) + 4)

    saturation = delta_pixel_val / max_pixel_val
    value = max_pixel_val

    return [hue, saturation, value]


def main():
    # Image format constants
    MagicSize = 16
    MagicValue = "P3\n"
    Depth = 3
    MaxLineLength = 70

    # Parses header
    magic_number = next(sys.stdin)
    if magic_number != MagicValue:
        print("error: invalid magic_number!", file=sys.stderr)
        sys.exit(1)

    try:
        sizes = next(sys.stdin).strip().split()
        width = int(sizes[0])
        height = int(sizes[1])
        if len(sizes)!=2 or width<=0 or height<=0:
            raise ValueError()
    except (IndexError, ValueError):
        print("error: invalid image sizes!", file=sys.stderr)
        sys.exit(1)

    try:
        maxval_line = next(sys.stdin).strip().split()
        maxval = int(maxval_line[0])
        if len(maxval_line) != 1 or maxval <= 0:
            raise ValueError()
    except (IndexError, ValueError):
        print("error: invalid image maximum pixel value!", file=sys.stderr)
        sys.exit(1)

    # Outputs parsed header
    print(MagicValue, end='')
    print("%d %d" % (width, height,))
    print("%d" % maxval)

    # Parses image contents
    line_length = 0
    next_values = []

    try:
        for row in range(height):
            for col in range(width):
                for channel in range(Depth):
                    if not next_values:
                        next_values = next(sys.stdin).strip().split()
                    raw_value = next_values.pop(0)
                    value = int(raw_value)
                    if value < 0 or value > maxval:
                        raise ValueError()
                    # Breaks long lines
                    length = get_decimal_length(value) + 1
                    if line_length+length > MaxLineLength:
                        print()
                        line_length = 0
                    # Outputs subpixel
                    print("%d " % value, end='')
                    line_length += length
    except IndexError:
        print("error: unexpected end of file!", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("error: invalid pixel value: %s!" % raw_value, file=sys.stderr)
        sys.exit(1)

    # ...breaks the last line if needed
    if line_length != 0:
        print()

if __name__ == "__main__":
    main()
