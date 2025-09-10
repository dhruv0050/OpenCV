import cv2

image = cv2.imread("image.jpg")
if image is not None:
    print("Image loaded successfully")
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading image")

## Resize the image to 300x200 pixels

resized = cv2.resize(image,(300,200))
cv2.imshow("Resized Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Image cropping

cropped_image = image[200:300, 100:200]
cv2.imshow("Cropped Image",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## image rotation

(h,w) = image.shape[:2]
center =(w//2, h//2)
M = cv2.getRotationMatrix2D(center,45,1.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated Image",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Image flipping

flipped_vertical = cv2.flip(image,0)
flipped_horizontal = cv2.flip(image,1)
flipped_vertical_horizontal = cv2.flip(image,-1)

cv2.imshow("Flipped Vertical",flipped_vertical)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Flipped Horizontal",flipped_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Flipped Vertical Horizontal",flipped_vertical_horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()