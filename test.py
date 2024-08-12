import numpy as np
import cv2
from PIL import Image

### read image base on image path
img = cv2.imread("test.jpg")

#### get shape of image
h,w = img.shape[:2]

### show image with pil format
Image.fromarray(img).show()

