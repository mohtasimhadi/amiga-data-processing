import cv2
from stitching import AffineStitcher

def stitch_image(images):
    stitcher = AffineStitcher(confidence_threshold=0.5)
    return stitcher.stitch(images)

def recursive_stitching(images, out_dir, stitching_factor = 32, iteration_factor = 16, epoch = 1):
    print(f"Total # of images in iteration {epoch}: {len(images)}")
    if len(images) == 1:
        cv2.imwrite("final_stitched.png", images[0])
        return images[0]
    rec_images = []
    for i in range(0, len(images)-1, iteration_factor):
        if i + stitching_factor > len(images):
            stitched_image = stitch_image(images[i:])
            rec_images.append(stitched_image)
            cv2.imwrite(f"{out_dir}/iteration_{str(epoch).zfill(2)}_image: {str(i).zfill(4)}:{str(len(images)).zfill(4)}.png", stitched_image)
            print(f"Iteration: {epoch}\tImage: {i}:{len(images)}")
        else:
            stitched_image = stitch_image(images[i:i+stitching_factor])
            rec_images.append(stitched_image)
            cv2.imwrite(f"{out_dir}/iteration_{str(epoch).zfill(2)}_image: {str(i).zfill(4)}:{str(i+stitching_factor).zfill(4)}.png", stitched_image)
            print(f"Iteration: {epoch}\tImage: {i}:{i+stitching_factor}")
    return recursive_stitching(rec_images, stitching_factor=3, iteration_factor=2, epoch=epoch+1)