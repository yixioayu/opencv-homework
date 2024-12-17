from operator import length_hint
import cv2
image = cv2.imread('work.jpg')
# Kernel=numpy.ones((3,3),numpy.uint8)
# gray=cv2.morphologyEx(image,cv2.MORPH_OPEN,Kernel)
gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
a,thresholded = cv2.threshold(blurred, 180, 255, cv2.THRESH_BINARY_INV)
contours,b = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
long=[]
for le in contours:
    length=cv2.arcLength(le,True)
    if length>200:
        long.append(le)
for l in long:
    cv2.drawContours(image, l, -1, (0, 255, 0), 3)
    imageresize=cv2.resize(image,(500,1000))
    cv2.imshow("Frame", imageresize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
area = cv2.contourArea(long[2])
print(area)