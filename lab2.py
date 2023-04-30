# Program for an image enhancement using pixel operation.

import cv2
import numpy as np

image = cv2.imread('./images/street.jpg')
image = cv2.resize(image, (512, 512))
cv2.imshow('Image', image)

ret, binary_thresh = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow('Binary', binary_thresh)

ret, inv_binary_thresh = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
cv2.imshow('Inverse Binary', inv_binary_thresh)

ret, to_zero_thresh = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_TOZERO)
cv2.imshow('To Zero', to_zero_thresh)

ret, inv_to_zero_thresh = cv2.threshold(image, thresh=127, maxval=255, type=cv2.THRESH_TOZERO_INV)
cv2.imshow('Inverse To Zero', inv_to_zero_thresh)

cv2.waitKey()
cv2.destroyAllWindows()
