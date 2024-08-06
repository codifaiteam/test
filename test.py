import numpy as np
import cv2
from PIL import Image

img = cv2.imread("test.jpg")
h,w = img.shape[:2]

Image.fromarray(img).show()

