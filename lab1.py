# Program to enhance image using image arithmetic and logical operations.

import cv2
import numpy as np

image = cv2.imread('./images/jar.jpeg')
image = cv2.resize(image, (512, 512))
cv2.imshow('Image', image)

noisy_images = []
for _ in range(20):
    img = image.copy()
    cv2.randn(img, (0,0,0), (50,50,50))
    noisy_images.append(image + img)
cv2.imshow('Noisy Image', noisy_images[0])

avg_img = np.zeros(image.shape, dtype=np.float32)
for i in noisy_images:
    avg_img = avg_img + i / len(noisy_images)
    avg_img = np.array(np.round(avg_img), dtype=np.uint8) # Addition
cv2.imshow('Average Image', avg_img)

matrix = np.ones(image.shape, dtype=np.uint8) * 100

dark_img = cv2.subtract(image, matrix) # Subrtraction
cv2.imshow('Dark Image', dark_img)

bright_img = cv2.multiply(image, matrix) # Multiplication
cv2.imshow('Bright Image', bright_img)


mask_image = cv2.imread('./images/circle.png')
mask_image = cv2.resize(mask_image, (512, 512))
cv2.imshow('Mask', mask_image)

and_img = cv2.bitwise_and(image, mask_image, mask=None) # AND
cv2.imshow('AND Operation', and_img)

or_img = cv2.bitwise_or(image, mask_image, mask=None) # OR
cv2.imshow('OR Operation', or_img)

not_mask = cv2.bitwise_not(mask_image, mask=None) # NOT
cv2.imshow('NOT Operation', not_mask)

xor_img = cv2.bitwise_xor(image, mask_image, mask=None) # XOR
cv2.imshow('XOR Operation', xor_img)

cv2.waitKey()
cv2.destroyAllWindows()
