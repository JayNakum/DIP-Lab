# Program for gray level slicing with and without background

import cv2
import numpy as np

image = cv2.imread('./images/street.jpg', 0)
image = cv2.resize(image, (512, 512))
cv2.imshow('Image', image)

LOWER_LIMIT = 50
UPPER_LIMIT = 150

output_img = np.zeros(image.shape, dtype=np.uint8)

for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if (image[i][j] > LOWER_LIMIT and image[i][j] < UPPER_LIMIT):
            output_img[i][j] = 255
        else:
            output_img[i][j] = 0 # Without Background
            # output_img[i][j] = image[i][j] # With Background

cv2.imshow('Gray Level Slicing', output_img)

cv2.waitKey()
cv2.destroyAllWindows()
