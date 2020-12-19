import cv2
import numpy as np

img_orig = cv2.imread('new.jpg')
print(img_orig)
# img_changed = cv2.imread('new_photo.png')
# difference = cv2.subtract(img_orig, img_changed)
# b, g, r = cv2.split(difference)
# if cv2.countNonZero(r) and cv2.countNonZero(g) and cv2.countNonZero(b) and img_orig.shape == img_changed.shape:
#     print(True)
# else:
#     print(False)