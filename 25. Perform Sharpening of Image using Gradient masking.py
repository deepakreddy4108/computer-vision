import cv2
import numpy as np
img = cv2.imread("D:\OpenCv\picture6.jpg")
if img is None:
    print("Error: Image not loaded.")
else:
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)
    gradient_mask = cv2.addWeighted(cv2.convertScaleAbs(sobelx), 0.5, cv2.convertScaleAbs(sobely), 0.5, 0)
    sharpened_img = cv2.addWeighted(gray_img, 2, gradient_mask, -1, 0)
    sharpened_img_bgr = cv2.cvtColor(sharpened_img.astype(np.uint8), cv2.COLOR_GRAY2BGR)
    cv2.imshow('Original Image', img)
    cv2.imshow('Sharpened Image using Gradient Masking', sharpened_img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
