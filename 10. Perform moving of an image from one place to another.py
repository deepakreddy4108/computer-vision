import cv2

# Load the image
image = cv2.imread("D:\OpenCv\picture6.jpg") 
if image is None:
    print('Error: Unable to load the image.')
    exit()
cv2.namedWindow('Moved Image', cv2.WINDOW_NORMAL)
cv2.imshow('Moved Image', image)
x, y = 100, 100
step = 5 
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  
        break
    if key == ord('w'): 
        y -= step
    elif key == ord('s'):  
        y += step
    elif key == ord('a'):  
        x -= step
    elif key == ord('d'):  
        x += step
    moved_image = image.copy()
    cv2.rectangle(moved_image, (x, y), (x + image.shape[1], y + image.shape[0]), (0, 255, 0), 2)
    cv2.imshow('Moved Image', moved_image)
cv2.destroyAllWindows()
