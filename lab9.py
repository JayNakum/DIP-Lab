# Program for illustrating color image processing

import cv2
import numpy as np

image = cv2.imread('./images/circles.png')
cv2.imshow('Image', image)

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_range = np.array([110, 50, 50])
upper_range = np.array([130, 255, 255])

mask = cv2.inRange(hsv_img, lower_range, upper_range)
cv2.imshow('Mask', mask)


color_mask = hsv_img.copy()
color_mask[:, :, 0] = color_mask[:, :, 0] * mask
color_mask[:, :, 1] = color_mask[:, :, 1] * mask
color_mask[:, :, 2] = color_mask[:, :, 2] * mask

cv2.imshow('Color Mask', color_mask)


cv2.waitKey()
cv2.destroyAllWindows()
