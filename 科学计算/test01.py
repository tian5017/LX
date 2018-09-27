import cv2

filename = "123.png"
img = cv2.imread(filename)
print(type(img), img.shape, img.dtype)

cv2.namedWindow("demo1")
cv2.imshow("demo1", img)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("demo2")
cv2.imshow("demo2", img_gray)
cv2.waitKey(0)
