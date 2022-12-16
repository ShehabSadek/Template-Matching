from Globals import *

def resize(scale_percent,src_img):
    width = int(src_img.shape[1] * scale_percent / 100)
    height = int(src_img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv.resize(src_img, dim, interpolation = cv.INTER_AREA)
