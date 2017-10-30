import cv2
import numpy as np

#load 2 images
img1 = cv2.imread('egimg1.png')
img2 = cv2.imread('egimg2.png')
#mergebothimages
#add = img1 + img2
#add = cv2.add(img1,img2)#addedallpixelvaluestogether
weighted = cv2.addWeighted(img1, 0.6, img2, 0,4,0)#imposing them on one another identically

cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
