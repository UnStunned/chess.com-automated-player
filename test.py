import cv2

image = cv2.imread('D:\Python Programming\Chess_Automation\screenshots\img.png')[100:200,0:100]


print(image[10,10])
cv2.imshow("image", image)
cv2.waitKey(2000)