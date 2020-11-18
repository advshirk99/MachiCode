import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sample=r'path_to_img\img2.jpg'
read_image= cv2.imread(sample,0)

#Converting into gray-scale image
convert_bin,grey_scale = cv2.threshold(read_image,110,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
grey_scale = 255-grey_scale
grey_graph = plt.imshow(grey_scale,cmap='gray')
plt.show()

#Finding horizontal lines of table
length = np.array(read_image).shape[1]//100
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (length, 1))
horizontal_detect = cv2.erode(grey_scale, horizontal_kernel, iterations=12)
hor_line = cv2.dilate(horizontal_detect, horizontal_kernel, iterations=15)
plotting = plt.imshow(horizontal_detect,cmap='gray')
plt.show()

#Finding vertical lines of table 
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, length))
vertical_detect = cv2.erode(grey_scale, vertical_kernel, iterations=7)
ver_lines = cv2.dilate(vertical_detect, vertical_kernel, iterations=9)
show = plt.imshow(vertical_detect,cmap='gray')
plt.show()

#Combining both masks to get entire table
final = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
combine = cv2.addWeighted(ver_lines, 0.5, hor_line, 0.5, 0.0)
combine = cv2.erode(~combine, final, iterations=2)
thresh, combine = cv2.threshold(combine,128,255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
convert_xor = cv2.bitwise_xor(read_image,combine)
inverse = cv2.bitwise_not(convert_xor)
output= plt.imshow(inverse,cmap='gray')
#plt.show()

cont, _ = cv2.findContours(combine, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
def get_boxes(num, method="left-to-right"):
    invert = False
    flag = 0
    if method == "right-to-left" or method == "bottom-to-top":
        invert = True
    if method == "top-to-bottom" or method == "bottom-to-top":
        flag = 1
    boxes = [cv2.boundingRect(c) for c in num]
    (num, boxes) = zip(*sorted(zip(num, boxes),
    key=lambda b:b[1][1], reverse=invert))
    return (num, boxes)
cont, boxes = get_boxes(cont, method="top-to-bottom")

#finding boundaries and cropping them according to the contours 
idx = 0
final_box = []
for c in cont:
    s1, s2, s3, s4 = cv2.boundingRect(c)
    if (s3<500 and s4<500):
        rectangle_img = cv2.rectangle(read_image,(s1,s2),(s1+s3,s2+s4),(0,255,0),2)
        final_box.append([s1,s2,s3,s4])
        idx+=1
        new_img=read_image[s2:s2+s4, s1:s1+s3]
        cv2.imwrite('D:\\Personal\\Practice\\CodeCell_Hackathon\\cropped\\new_croppedi'+str(idx) + '.png', new_img)
plt.imshow(rectangle_img,cmap='gray')
plt.title("Table-Contour")
plt.show()
