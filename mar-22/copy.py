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
