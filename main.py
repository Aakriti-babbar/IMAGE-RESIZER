import cv2
source = "aakriti.jpg"
destination = "newImage.jpg"
scale_percent = 80
image = cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",image)

#calculate the 50 percent of original dimensions

new_w = int(image.shape[1] * scale_percent / 100)
new_h = int(image.shape[0] * scale_percent / 100)

#resize image

output = cv2.resize(image , (new_w , new_h))
cv2.imwrite(destination , output)

cv2.waitKey(0)
