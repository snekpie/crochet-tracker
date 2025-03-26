from PIL import Image

from PIL import Image

def pixelate_image_to_stitch_grid(image_path, grid_size, stitch_type='sc', base_width=10):
    """
    Pixelates an image into a grid and stretches each pixel based on stitch type.
    
    Parameters:
        image_path (str): Path to the image file.
        grid_size (tuple): (cols, rows) — number of stitch blocks
        stitch_type (str): Type of crochet stitch (e.g., 'sc', 'hdc', 'dc')
        base_width (int): Width in pixels of a single stitch (defaults to 10)
        
    Returns:
        PIL.Image: Resized pixelated image for visualization.
    """
    # Define pixel height ratios for different stitches
    stitch_ratios = {
        'sc': 1.0,
        'hdc': 1.3,
        'dc': 1.6,
        'tr': 2.0,  # if needed in future
    }

    # Determine output pixel size based on stitch type
    ratio = stitch_ratios.get(stitch_type, 1.0)
    block_w = base_width
    block_h = int(base_width * ratio)

    img = Image.open(image_path).convert("RGB")

    # Step 1: Resize down to grid
    small = img.resize(grid_size, resample=Image.NEAREST)

    # Step 2: Stretch up using calculated stitch dimensions
    cols, rows = grid_size
    out_w = cols * block_w
    out_h = rows * block_h
    stretched = small.resize((out_w, out_h), Image.NEAREST)

    return stretched

# pattern extraction
def extract_pattern_from_image(image_path, stitch_type='sc', grid_size=(60, 40)):
    """
    Extracts a pattern from a pixelated image based on a known stitch grid size.

    Parameters:
        image_path (str): Path to the image.
        stitch_type (str): Type of stitch to assign.
        grid_size (tuple): (cols, rows) = number of stitches across and down.

    Returns:
        list: Pattern as a list of row dictionaries.
    """
    img = Image.open(image_path).convert('RGB')

    # Step 1: Resize image to match expected grid size
    img = img.resize(grid_size, resample=Image.NEAREST)

    pattern = []

    for y in range(grid_size[1]):
        row_stitches = []
        current_color = rgb_to_hex(img.getpixel((0, y)))
        group = [(current_color, stitch_type)]

        for x in range(1, grid_size[0]):
            color = rgb_to_hex(img.getpixel((x, y)))
            if color == current_color:
                group.append((color, stitch_type))
            else:
                row_stitches.extend(group)
                current_color = color
                group = [(color, stitch_type)]

        row_stitches.extend(group)
        pattern.append({'row': y + 1, 'stitches': row_stitches})
    
    pattern.reverse()
    return pattern

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)
