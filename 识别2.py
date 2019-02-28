import cv2
import numpy as np

camera = cv2.VideoCapture("1.avi")
mog = cv2.createBackgroundSubtractorMOG2()

while True:
    ret,frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask,5)#中值滤波
    th2 = cv2.threshold(blur,127,255,cv2.THRESH_BINARY)[1]#阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    eroded_2 = cv2.erode(th2,kernel,iterations = 2)
    eroded_1 = cv2.erode(th2,kernel,iterations = 1)
    dilated = cv2.dilate(eroded_2,kernel,iterations = 2)
    image, contours, gihr = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
                                                                                                    #参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
        #计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        if cv2.contourArea(c) > 100:
            (x,y,w,h) = cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)#图像加框，参数1：图像，参数2：左上角坐标，参数3：右下角坐标，参数4：框的颜色，参数5：框的粗细
			

    #腐蚀
    cv2.imshow("eroded_1",eroded_1)
    cv2.imshow("dilated",dilated)
    cv2.imshow("detection",frame)
    #cv2.imshow("th2",th2)
    if cv2.waitKey(24) & 0xff == 27:
        break
camera.release()
cv2.destroyAllWindows()

#使用高斯混合模型对背景建模，取出前景

#使用中值滤波去除椒盐噪声，再闭运算填充空洞


