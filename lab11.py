# Program for image watermarking

import cv2

img = cv2.imread('./images/street.jpg')
watermark = cv2.imread('./images/new_watermark.jpeg', cv2.IMREAD_UNCHANGED)

watermark = cv2.resize(watermark, (img.shape[1], img.shape[0]))

alpha = 0.5  # set the opacity of the watermark
dst = cv2.addWeighted(img, 1-alpha, watermark, alpha, 0)

cv2.imshow('Flitered Image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
