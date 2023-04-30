# Program for sharp image using ideal high pass filter in frequency domain

import cv2
import numpy as np
import matplotlib.pyplot as plt

def plt_imshow(title:str, image:cv2.Mat, cmap='gray'):
    plt.title(title)
    plt.imshow(image, cmap)
    plt.axis('off')
    plt.show()

image = cv2.imread('./images/cube.png', 0)
plt_imshow('Image', image)

fourier = np.fft.fft2(image)
# plt_imshow('Fourier Transform', np.log1p(np.abs(fourier)))

shift_fourier = np.fft.fftshift(fourier)
# plt_imshow('Shifting', np.log1p(np.abs(shift_fourier)))

m, n = image.shape
filter = np.zeros(image.shape, dtype=np.float32) # Ideal Filter: H(u, v)
D0 = 50
for u in range(m):
    for v in range(n):
        D = np.sqrt((u-m/2)**2 + (v-n/2)**2)
        if D > D0:
            filter[u, v] = 0
        else:
            filter[u, v] = 1
filter = 1 - filter # HIGH PASS FILTER
plt_imshow('Filter', filter)

shift_filtered_fourier = shift_fourier * filter
# plt_imshow('Filter Applied', np.log1p(np.abs(shift_filtered_fourier)))

filtered_fourier = np.fft.ifftshift(shift_filtered_fourier)
# plt_imshow('Inverse Shifting', np.log1p(np.abs(filtered_fourier)))

filtered_img = np.fft.ifft2(filtered_fourier)
plt_imshow('Filtered Image', np.abs(filtered_img))

cv2.waitKey()
cv2.destroyAllWindows()
