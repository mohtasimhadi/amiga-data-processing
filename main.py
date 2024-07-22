import os, cv2
from modules.image_stitcher.stitcher import recursive_stitching

output_direction = "out"
input_direction = "frames"

directory = 'frames'
images = []
images_directories = os.listdir(directory)
images_directories.sort()

for filename in images_directories:
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        img_path = os.path.join(directory, filename)
        img = cv2.imread(img_path)
        if img is not None:
            images.append(img)
            print(f"Loaded: {img_path}")
print("End of loading!")

recursive_stitching(images)