import re

def parse_crochet_pattern(filename):
    pattern = []

    # Regular expression patterns
    row_regex = re.compile(r'R(\d+):\s*(.*)')
    color_stitch_regex = re.compile(r'(\w+)\s*\[([^\]]+)\]')

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()         # remove empty spaces before and after rows
            if not line:
                continue                # skip empty lines
            
            # Parse row number and stitch data
            row_match = row_regex.match(line)
            if not row_match:
                raise ValueError(f"Line format incorrect: {line}")

            row_num = int(row_match.group(1))   # returns the int value of the first group, which is the row number
            stitches_data = row_match.group(2)  # returns everything else (stitches)

            # Find color and stitch groups
            stitches = []
            for color_match in color_stitch_regex.finditer(stitches_data):
                color = color_match.group(1)
                stitch_list = [s.strip() for s in color_match.group(2).split(',')]

                for stitch in stitch_list:
                    stitches.append((color, stitch))

            pattern.append({'row': row_num, 'stitches': stitches})

    return pattern
