import os
import numpy as np
from skimage import io, color, measure, util, morphology

def extract_roi(image, y1, x1, y2, x2):
    return image[y1:y2, x1:x2]

def check_if_bottle_cap_missing(image):
    image = util.img_as_ubyte(image)
    image_gray = color.rgb2gray(image)
    roi = extract_roi(image_gray, 5, 150, 45, 200)
    roi_binary = roi < 150/256
    black_percentage = np.sum(roi_binary == 0) / roi.size * 100
    return black_percentage > 90

def check_if_bottle_deformed(image):
    image = util.img_as_ubyte(image)
    
    cropped_img = image[100:191, 260:281, :]
    
    img_red = cropped_img[:, :, 0]
    
    label_bin_red = img_red > 100
    
    black_pixels = np.sum(label_bin_red == 0)
    total_pixels = label_bin_red.size
    percentage = 100 * (black_pixels / total_pixels)

    if percentage > 80:
        mask = color.rgb2gray(cropped_img)
        label_bin_gs = mask > 5

        labeled_image = morphology.label(label_bin_gs, connectivity=2)
    else:
        labeled_image = morphology.label(label_bin_red, connectivity=2)

    properties = measure.regionprops(labeled_image)

    max_area = 0
    max_box_height = 0

    for prop in properties:
        min_row, min_col, max_row, max_col = prop.bbox
        bb_width = max_col - min_col
        bb_height = max_row - min_row
        bb_area = bb_width * bb_height

        if bb_area > max_area:
            max_area = bb_area
            max_box_height = bb_height

    bottle_deformed = max_box_height > 60

    return bottle_deformed

def check_if_bottle_missing(image):
    image = util.img_as_ubyte(image)
    image_gray = color.rgb2gray(image)
    roi = extract_roi(image_gray, 1, 135, 250, 225)
    roi_binary = roi < 150/256
    black_percentage = np.sum(roi_binary == 0) / roi.size * 100
    return black_percentage > 90

def check_if_bottle_overfilled(image):
    image = util.img_as_ubyte(image)
    image_gray = color.rgb2gray(image)
    roi = extract_roi(image_gray, 110, 140, 140, 220)
    roi_binary = roi < 150/256
    black_percentage = np.sum(roi_binary == 0) / roi.size * 100
    return black_percentage < 1

def check_if_bottle_underfilled(image):
    image = util.img_as_ubyte(image)
    image_gray = color.rgb2gray(image)
    roi = extract_roi(image_gray, 110, 140, 140, 220)
    roi_binary = roi < 150/256
    black_percentage = np.sum(roi_binary == 0) / roi.size * 100
    return black_percentage == 100

def check_if_label_missing(image):
    image = util.img_as_ubyte(image)
    image_gray = color.rgb2gray(image)
    roi = extract_roi(image_gray, 180, 110, 280, 240)
    roi_binary = roi < 50/256
    black_percentage = np.sum(roi_binary == 0) / roi.size * 100
    return black_percentage < 10

def check_if_label_not_printed(image):
    image = util.img_as_ubyte(image)
    image_gray = color.rgb2gray(image)
    roi = extract_roi(image_gray, 180, 110, 280, 240)
    roi_binary = roi < 150/256
    black_percentage = np.sum(roi_binary == 0) / roi.size * 100
    return black_percentage > 80

def check_if_label_not_straight(image):
    image = util.img_as_ubyte(image)
    image_gray = color.rgb2gray(image)
    roi = extract_roi(image_gray, 180, 110, 280, 240)
    roi_binary = roi < 30/256
    black_percentage = np.sum(roi_binary == 0) / roi.size * 100
    return (black_percentage > 70 and black_percentage < 95)


images_dir = r'Your File Path'

file_names = os.listdir(images_dir)

output_file_path = 'Output.txt'

with open(output_file_path, 'w') as output_file:
    for file_name in file_names:
        if file_name.lower().endswith('.jpg'):
            file_path = os.path.join(images_dir, file_name)
            image = io.imread(file_path)

            detected_faults = []

            if check_if_bottle_missing(image):
                output_file.write(f'{file_name}: Bottle Missing\n')
            else:
                if check_if_bottle_cap_missing(image):
                    detected_faults.append('Bottle Cap Missing')
                if check_if_bottle_deformed(image):
                    detected_faults.append('Bottle Deformed')
                if check_if_bottle_overfilled(image):
                    detected_faults.append('Bottle Overfilled')
                if check_if_bottle_underfilled(image):
                    detected_faults.append('Bottle Underfilled')
                if check_if_label_missing(image):
                    detected_faults.append('Label Missing')
                if check_if_label_not_printed(image):
                    detected_faults.append('Label Not Printed')
                if check_if_label_not_straight(image):
                    detected_faults.append('Label Not Straight')

                if detected_faults:
                    output_file.write(f'{file_name}: Detected Faults: {", ".join(detected_faults)}\n')
                else:
                    output_file.write(f'{file_name}: No Faults Detected\n')
        else:
            output_file.write(f'Skipping file: {file_name} (not a JPG image)\n')