# Room Map Processing

This project processes a `.pgm` map file using information from a corresponding `.yaml` file and extracts structural features using image processing techniques. The output includes vector representations of the map in SVG and DXF formats, as well as an image visualization of detected edges.

## Features

- Reads `.pgm` map images
- Uses `.yaml` metadata for real-world scaling
- Applies adaptive thresholding and morphological operations
- Detects edges using the Canny edge detector
- Extracts structured features using Hough Line Transform
- Saves results as:
  - **SVG**: Scalable vector representation
  - **DXF**: CAD-compatible format
  - **PNG**: Visualization of detected edges

## Requirements

Ensure you have the following dependencies installed:

```bash
pip install opencv-python numpy matplotlib ezdxf pyyaml
```

## Usage

1. Place your `.pgm` and `.yaml` files in the working directory.
2. Update the file paths in the script if necessary:
   ```python
   pgm_file = "room2.pgm"
   yaml_file = "room1.yaml"
   ```
3. Run the script:
   ```bash
   python process_map.py
   ```
4. Output files will be generated in the same directory:
   - `room2.svg`: Vector representation
   - `room2.dxf`: DXF format for CAD software
   - `room2.png`: Edge-detected visualization

## Output Example

- **SVG/DXF Output**: Lines representing walls and structures extracted from the map.
- **PNG Output**: A grayscale image highlighting detected edges.

## Notes

- Ensure the YAML file contains correct metadata (`resolution`, `origin`).
- The script flips the Y-axis to align with real-world coordinates.
- The Hough Transform parameters can be adjusted for better line detection.

## License

This project is open-source and can be modified as needed(is part of a interview).

## Improvements
This project further requires some precise improvements to recreate a CAD produced image.

## Author

Ashin


