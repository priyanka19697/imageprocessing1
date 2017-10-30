import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (0,0,0), 15 )
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)
cv2.circle(img, (100,63), 55, (0,0,255), -1)  ##-1 fills in the circle

pts = np.array([[10,5], [20,30], [70,20 ], [50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True,(0,255,255), 5 )

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'opencv TUTS!', (0,130), font, 6, (200,0,0), 5, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()