# Bottle Inspection System

This project is an image inspection system designed to detect various faults in images of bottles. It includes functions to analyze images and determine if certain faults are present. The faults that the system detects include missing bottle caps, deformed bottles, overfilled or underfilled bottles, missing labels, labels not printed, and labels not straight.

## Requirements

- Python 3.x
- NumPy
- scikit-image

## Usage

1. Clone the repository or download the source files.

2. Ensure that you have Python installed on your system along with the required libraries (`NumPy` and `scikit-image`).

3. Place your images in a directory and update the `images_dir` variable in the script with the path to your image directory.

4. Run the script. It will analyze each image in the specified directory and generate an output file (`Output.txt`) listing any detected faults.

## Functions

- `extract_roi(image, y1, x1, y2, x2)`: Extracts a region of interest (ROI) from the given image based on the specified coordinates.

- `check_if_bottle_cap_missing(image)`: Checks if the bottle cap is missing in the image.

- `check_if_bottle_deformed(image)`: Checks if the bottle is deformed.

- `check_if_bottle_missing(image)`: Checks if the bottle is missing.

- `check_if_bottle_overfilled(image)`: Checks if the bottle is overfilled.

- `check_if_bottle_underfilled(image)`: Checks if the bottle is underfilled.

- `check_if_label_missing(image)`: Checks if the label is missing.

- `check_if_label_not_printed(image)`: Checks if the label is not printed.

- `check_if_label_not_straight(image)`: Checks if the label is not straight.

## Output

The system generates an output file named `Output.txt`, which contains the analysis results for each image processed. Each line of the output file corresponds to an image and indicates whether any faults were detected or if the image is free from faults.

## Notes

- Ensure that the images are in JPG format for proper analysis.

- The system uses thresholding and morphological operations to detect faults in the images. Adjustments may be necessary depending on the characteristics of the images being analyzed.

- Make sure to review the output file for the analysis results of each image.

## Disclaimer

This project is provided as-is without any warranty. It is intended for educational and demonstration purposes only.
