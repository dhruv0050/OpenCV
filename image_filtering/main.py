import cv2
import numpy as np

## Practically Applying Gaussian Blur to image
image1 = cv2.imread("free-nature-images.jpg")
blurred_image = cv2.GaussianBlur(image1,(7,7),3)
cv2.imshow("Original Image",image1)
cv2.imshow("Gaussian Blurred Image",blurred_image)
cv2.waitKey(0)  
cv2.destroyAllWindows()

## Practically Applying Median Blur to image
image2 = cv2.imread("noisy_f.png")
median_blurred_image = cv2.medianBlur(image2,7)
cv2.imshow("Original Image",image2)
cv2.imshow("Median Blurred Image",median_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Practically applying sharpness to image
image3 = cv2.imread("low_r.png")
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
sharpened_image = cv2.filter2D(image3,-1,kernel)
cv2.imshow("Original Image",image3)
cv2.imshow("Sharpened Image",sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()