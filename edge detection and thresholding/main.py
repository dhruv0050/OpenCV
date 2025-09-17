import cv2
import numpy as np
# Edge detection
img = cv2.imread('flower.png', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img,50,150)
cv2.imshow('Edges', edges)
cv2.waitKey(0)  
cv2.destroyAllWindows()

# Thresholding

img1 = cv2.imread('man.png', cv2.IMREAD_GRAYSCALE)
ret,thresh_img = cv2.threshold(img1,120,255,cv2.THRESH_BINARY)
cv2.imshow('Thresholded', thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bitwise operations
img2 = np.zeros((300,300), dtype="uint8")
cv2.rectangle(img2, (100,100), (250,250), 255, -1)
cv2.imshow('Rectangle', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = np.zeros((300,300), dtype="uint8")
cv2.circle(img3, (150,150), 75, 255, -1)
cv2.imshow('Circle', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

and_op = cv2.bitwise_and(img2, img3)
cv2.imshow('AND Operation', and_op)
cv2.waitKey(0)
cv2.destroyAllWindows()

or_op = cv2.bitwise_or(img2, img3)
cv2.imshow('OR Operation', or_op)
cv2.waitKey(0)
cv2.destroyAllWindows()

not_op = cv2.bitwise_not(img2)
cv2.imshow('NOT Operation', not_op)
cv2.waitKey(0)
cv2.destroyAllWindows()

xor_op = cv2.bitwise_xor(img2, img3)
cv2.imshow('XOR Operation', xor_op) 
cv2.waitKey(0)
cv2.destroyAllWindows()