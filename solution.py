import cv2
import numpy as np
import matplotlib.pyplot as plt
import ezdxf
import yaml

# File paths
pgm_file = "room2.pgm"
yaml_file = "room1.yaml"
output_svg = "room2.svg"
output_dxf = "room2.dxf"
output_png="room2.png"

# Load the YAML file
with open(yaml_file, 'r') as f:
    yaml_data = yaml.safe_load(f)

resolution = yaml_data["resolution"]  # Meters per pixel
origin = yaml_data["origin"][:2]  # X, Y origin

# Load the PGM file
image = cv2.imread(pgm_file, cv2.IMREAD_GRAYSCALE)

# Adaptive thresholding for better binarization
binary_map = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

# Morphological operations to enhance edges
kernel = np.ones((3, 3), np.uint8)
binary_map = cv2.morphologyEx(binary_map, cv2.MORPH_CLOSE, kernel, iterations=2)

# Edge detection using Canny
edges = cv2.Canny(binary_map, 50, 150)

# Hough Line Transform for structured features
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=10, maxLineGap=5)

# Scaling function
def scale_point(pt):
    """ Convert pixel coordinates to real-world coordinates using resolution and origin """
    x = origin[0] + pt[0] * resolution
    y = origin[1] + (image.shape[0] - pt[1]) * resolution  # Flip Y-axis
    return (x, y)

# Convert detected lines to SVG
with open(output_svg, "w") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">')
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            x1, y1 = scale_point((x1, y1))
            x2, y2 = scale_point((x2, y2))
            f.write(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="black" />\n')
    f.write('</svg>')

# Convert detected lines to DXF format
doc = ezdxf.new()
msp = doc.modelspace()
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        msp.add_line(scale_point((x1, y1)), scale_point((x2, y2)))

doc.saveas(output_dxf)

# Display processed edges and detected lines
plt.figure(figsize=(8, 8))
plt.imshow(edges, cmap="gray")
plt.title("Detected Edges with Hough Transform")
plt.axis("off")
# Save the figure before showing it
plt.savefig(output_png, bbox_inches="tight", dpi=300)
plt.show()
print(f"PNG saved at: {output_png}")

print(f"SVG saved at: {output_svg}")
print(f"DXF saved at: {output_dxf}")
