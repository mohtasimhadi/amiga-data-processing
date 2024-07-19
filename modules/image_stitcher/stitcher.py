from stitching import AffineStitcher

def stitch_image(images):
    stitcher = AffineStitcher(detector='sift', confidence_threshold=0.01)
    return stitcher.stitch(images)