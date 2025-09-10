import cv2

image = cv2.imread("image.png")
if image is not None:
    print("Image loaded successfully")
    cv2.imshow("Image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error loading image")

print(image.shape)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",gray)
cv2.waitKey(0)  
cv2.destroyAllWindows()

if gray is not None:
    cv2.imwrite("gray_image.png", gray)
    print("Gray image saved successfully")
else:
    print("Error converting image to grayscale")