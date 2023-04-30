# Program for morphological image operations (erosion, dilation, opening, closing)

import cv2
import numpy as np

image = cv2.imread('./images/lady.png', 0)
cv2.imshow('Image', image)

kernel = np.ones((5, 5), dtype=np.uint8)

erosion_img = cv2.erode(image, kernel, iterations=1)
cv2.imshow('Erosion', erosion_img)

dilation_img = cv2.dilate(image, kernel, iterations=1)
cv2.imshow('Dilation', dilation_img)

opening_img = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel, iterations=1)
cv2.imshow('Opening', opening_img)

closing_img = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel, iterations=1)
cv2.imshow('Closing', closing_img)

cv2.waitKey()
cv2.destroyAllWindows()
