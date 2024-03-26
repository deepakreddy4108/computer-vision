import cv2 
path ="D:\OpenCv\Picture5.jpg"
src = cv2.imread(path) 
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180) 
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
import cv2 
path ="D:\OpenCv\Picture3.jpg"
src = cv2.imread(path) 
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) 
 # Displaying the image 
cv2.imshow(window_name, image) 
cv2.waitKey(0) 
import cv2 
path = "D:\OpenCv\Picture4.jpg"
src = cv2.imread(path) 
window_name = 'Image' 
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) 
cv2.imshow(window_name, image) 
cv2.waitKey(0)
