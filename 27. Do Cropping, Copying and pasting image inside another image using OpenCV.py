import cv2
import numpy as np
# Load the main image (where you want to paste the cropped image)
main_image = cv2.imread("D:\OpenCv\Dhoni&Kohli.jpg")

# Load the image to be cropped and pasted
crop_image = cv2.imread("D:\OpenCv\Dhoni.jpg")
# Define the region of interest (ROI) in the main image where you want to paste the cropped image
x, y, w, h = 100, 100, 200, 200  # Example coordinates (adjust as needed)
roi = main_image[y:y+h, x:x+w]
# Resize the cropped image to fit the ROI
crop_image_resized = cv2.resize(crop_image, (w, h))
# Copy the resized cropped image and paste it into the ROI of the main image
main_image[y:y+h, x:x+w] = crop_image_resized
# Display the modified image
cv2.imshow('Modified Image', main_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the modified image
cv2.imwrite('path/to/output_image.jpg', main_image)
