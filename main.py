from pattern_parser import parse_crochet_pattern
from visualizer import visualize_crochet_pattern
from image_tools import pixelate_image_to_stitch_grid
from image_tools import extract_pattern_from_image
import matplotlib.pyplot as plt

# Example 1: Parse and visualize a text pattern
#pattern = parse_crochet_pattern("testpattern.txt")
#visualize_crochet_pattern(pattern)

# Example 2: Pixelate an image and save it
pixelated = pixelate_image_to_stitch_grid(
    image_path="buildings.jpg",
    grid_size=(100, 100),
    stitch_type='dc',
    base_width=10
)
pixelated.save("pixelated_image.png")
#plt.imshow(pixelated)
#plt.axis('off')
#plt.show()

# Example 3: Extract pattern from the pixelated image
generated_pattern = extract_pattern_from_image("pixelated_image.png", stitch_type='sc')

# Save the generated pattern as a .txt file
with open("generated_pattern.txt", "w") as f:
    for row in generated_pattern:
        f.write(f"R{row['row']}: ")
        current_color = None
        group = []

        for color, stitch in row['stitches']:
            if color == current_color:
                group.append(stitch)
            else:
                if group:
                    f.write(f"{current_color} [{', '.join(group)}] ")
                current_color = color
                group = [stitch]

        if group:
            f.write(f"{current_color} [{', '.join(group)}]")

        f.write("\n")

# Optional: Visualize the newly generated pattern
visualize_crochet_pattern(generated_pattern)
