# Drawing shapes and text on images using OpenCV

import cv2

image = cv2.imread("image1.jpg")

## Drwaing line to the image - image1

pt1 = (50,100)
pt2 = (300,100)
cv2.line(image,pt1,pt2,(0,255,0),2)

cv2.imshow("Line drawing",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Drawing rectangle to the image - image2
pt1 = (80,50)
pt2 = (300,220)
cv2.rectangle(image,pt1,pt2,(0,0,255),2)
cv2.imshow("Rectangle drawing",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Drawing circle to the image - image3
center = (200,120)
radius = 100
cv2.circle(image,center,radius,(255,0,0),2)
cv2.imshow("Circle drawing",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Drawing text to the image - image4
text = "Boy"
org = (50,150)
cv2.putText(image,text,org,fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,0,255),thickness=5)
cv2.imshow("Text drawing",image)
cv2.waitKey(0)
cv2.destroyAllWindows()