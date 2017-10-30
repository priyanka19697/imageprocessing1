import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55,55]

print(px)

img[55,55] = [0,0,0]
px = img[55,55]
print(px)

#regionofimage
#codetocopyaregionofimagetoanother
#watch_face = img[particular region]
#img[another region of same size] = watch_face

roi = img[100:150, 100:150]
print(roi)

img[100:150,100:150] = [0,0,0]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
