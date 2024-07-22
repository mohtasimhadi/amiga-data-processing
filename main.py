import os, cv2
from modules.image_stitcher.stitcher import recursive_stitching

output_direction = "out_2"
input_direction = "out"

images = []
images_directories = os.listdir(input_direction)
images_directories.sort()

for filename in images_directories:
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img_path = os.path.join(input_direction, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
            print(f"Loaded: {img_path}")
print("End of loading!")

recursive_stitching(images, out_dir=output_direction, stitching_factor=16)