import matplotlib.pyplot as plt
from pattern_parser import parse_crochet_pattern

stitch_heights = {'sc': 1, 'hdc': 1.3, 'dc': 1.6}
def visualize_crochet_pattern(pattern):
    # Determine grid size
    max_width = max(len(row['stitches']) for row in pattern)
    height = sum(stitch_heights.get(stitch, 1) for row in pattern for _, stitch in row['stitches']) # if the stitch isn't defined in the dictionary, the default height value is 1
    scale = 0.5
    fig, ax = plt.subplots(figsize=(max_width * scale, height*scale))
    y_offset = 0
    
    for row in pattern:
        x_offset = 0
        row_height = max(stitch_heights.get(stitch, 1) for _, stitch in row['stitches'])
        for color, stitch in row['stitches']:
            rect = plt.Rectangle((x_offset, y_offset), 1, stitch_heights.get(stitch, 1), facecolor=color, edgecolor='black')
            ax.add_patch(rect)
            x_offset += 1
        y_offset += row_height
    
    ax.set_xlim(0, max_width)
    ax.set_ylim(0, y_offset)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    plt.show()


#pattern = parse_crochet_pattern('testpattern.txt')
#visualize_crochet_pattern(pattern)

