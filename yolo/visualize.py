import cv2
import os
from pathlib import Path

# Paths to your folders
image_dir = '/Users/javereja/Desktop/Machine Learning/split2/train/images'
label_dir = '/Users/javereja/Desktop/Machine Learning/split2/train/labels'

# Output folder (optional)
output_dir = '/Users/javereja/Desktop/Machine Learning/output_visuals'
os.makedirs(output_dir, exist_ok=True)

# Loop through all images
for img_name in os.listdir(image_dir):
    if not img_name.endswith('.jpg'):
        continue

    image_path = os.path.join(image_dir, img_name)
    label_path = os.path.join(label_dir, img_name.replace('.jpg', '.txt'))

    # Read image
    img = cv2.imread(image_path)
    h, w, _ = img.shape

    # Read label file
    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            cls, x_center, y_center, bw, bh = map(float, line.strip().split())
            # Convert from YOLO format to pixel coordinates
            x1 = int((x_center - bw / 2) * w)
            y1 = int((y_center - bh / 2) * h)
            x2 = int((x_center + bw / 2) * w)
            y2 = int((y_center + bh / 2) * h)

            # Draw rectangle and class label
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img, f'Class {int(cls)}', (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Save or show the image
    out_path = os.path.join(output_dir, img_name)
    cv2.imwrite(out_path, img)