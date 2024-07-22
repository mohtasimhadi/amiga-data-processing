import cv2
from stitching import AffineStitcher

def stitch_image(images):
    stitcher = AffineStitcher(detector='sift', confidence_threshold=0.01)
    return stitcher.stitch(images)

def recursive_stitching(images, out_dir, stitching_factor = 32, iteration = 1):
    print(f"Total # of images in iteration {iteration}: {len(images)}")
    if len(images) == 1:
        cv2.imwrite("final_stitched.png", images[0])
        return images[0]
    rec_images = []
    for i in range(0, len(images)-1, stitching_factor):
        if i + stitching_factor > len(images):
            stitched_image = stitch_image(images[i:])
            rec_images.append(stitched_image)
        stitched_image = stitch_image(images[i:i+stitching_factor])
        rec_images.append(stitched_image)
        cv2.imwrite(f"{out_dir}/iteration_{iteration}_image: {i}:{i+stitching_factor}.png", stitched_image)
        print(f"Iteration: {iteration}\tImage: {i}:{i+stitching_factor}")
    if stitching_factor / 2 == 1:
        return recursive_stitching(rec_images, stitching_factor, iteration=iteration+1)
    else:
        return recursive_stitching(rec_images, stitching_factor/2, iteration=iteration+1)