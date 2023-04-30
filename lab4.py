# Program for image enhancement using historgam equalization

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('./images/street.jpg', 0)
image = cv2.resize(image, (512, 512))
cv2.imshow('Image', image)

histogram = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(histogram)

equalized_img = cv2.equalizeHist(image)

histogram = cv2.calcHist([equalized_img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
plt.plot(histogram)

cv2.imshow('Equalization', equalized_img)
plt.show()

# cv2.waitKey()
cv2.destroyAllWindows()
