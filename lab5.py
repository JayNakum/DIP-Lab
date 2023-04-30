# Program to filter an image using image averaging low pass filter in spatial domain and median filter

import cv2
import numpy as np

image = cv2.imread('./images/tree.jpeg')
cv2.imshow('Image', image)

# low pass filter
kernel5 = np.ones((5, 5), dtype=np.uint8) / 25 # 5 x 5 filter
kernel11 = np.ones((11, 11), dtype=np.uint8) / 121 # 11 x 11 filter

blur_img1 = cv2.filter2D(image, ddepth=-1, kernel=kernel5)
cv2.imshow('Blur Image (5 x 5)', blur_img1)

blur_img2 = cv2.filter2D(image, ddepth=-1, kernel=kernel11)
cv2.imshow('Blur Image (11 x 11)', blur_img2)

cv2.waitKey()
cv2.destroyAllWindows()

# median filter
image = cv2.imread('./images/spnimg.jpg', 0)
cv2.imshow('Image', image)

m, n = image.shape

filtered_img = np.zeros(image.shape, dtype=np.uint8)

for i in range(1, m-1):
    for j in range(1, n-1):
        temp = [
            image[i-1, j-1],
            image[i-1, j],
            image[i-1, j+1],
            image[i, j-1],
            image[i, j],
            image[i, j+1],
            image[i+1, j-1],
            image[i+1, j],
            image[i+1, j+1],
        ]
        temp = sorted(temp)
        filtered_img[i, j] = temp[4]

filtered_img = filtered_img.astype(np.uint8)
cv2.imshow('Filtered Image', filtered_img)

cv2.waitKey()
cv2.destroyAllWindows()
