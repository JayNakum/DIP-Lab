# Program for detecting edges in an image using roberts cross gradient operator and sobel operator

import cv2
import numpy as np

image = cv2.imread('./images/book.jpeg')
cv2.imshow('Image', image)

grayscale_img = cv2.cvtColor(image, code=cv2.COLOR_BGR2GRAY)

roberts_kernel = np.array([
    [1, 0],
    [0, -1]
], dtype=np.float32)
roberts_img = cv2.filter2D(grayscale_img, ddepth=-1, kernel=roberts_kernel)
cv2.imshow('Roberts Operator', roberts_img)

sobel_img = cv2.Sobel(grayscale_img, ddepth=-1, dx=1, dy=0, ksize=3)
cv2.imshow('Sobel Operator', sobel_img)

cv2.waitKey()
cv2.destroyAllWindows()
