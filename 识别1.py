import cv2
import numpy as np

bs = cv2.createBackgroundSubtractorKNN()#k-Nearest Neighbor分类算法
camera = cv2.VideoCapture("1.avi")#导入视频，括号中为视频地址，0表示打开笔记本内置摄像头
 
while True:
	ret, frame = camera.read()#ret为布尔值，当读取至视频最后一帧后，返回False
				  #frame为每一帧图像的三维矩阵
	fgmask = bs.apply(frame)
	fg2 = fgmask.copy()
	blur = cv2.medianBlur(fg2,5)#中值滤波
	th = cv2.threshold(blur,254,255,cv2.THRESH_BINARY)[1]#图像的简单阈值处理，第一个参数：原图像，第二个参数：进行分类的阈值，第三个参数：高于（低于）阈值时赋予的新值，第四个参数：选择参数的方法
							    #第一个返回值：得到的阈值，第二个阈值：阈值化后的图像。此处只取第二个返回值，加[1]
	dilated = cv2.dilate(th,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3)),iterations = 2)#膨胀的次数
			     #图像的膨胀
	image, contours, gihr = cv2.findContours(dilated,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)#提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
												    #参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
	#计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
	for c in contours:
		if cv2.contourArea(c) > 100:
			(x,y,w,h) = cv2.boundingRect(c)
			cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)#图像加框，参数1：图像，参数2：左上角坐标，参数3：右下角坐标，参数4：框的颜色，参数5：框的粗细
			cv2.rectangle(frame,(250,250),(500,500),(255,255,0),2)
			if x > 200 and y >200:
				cv2.rectangle(frame,(x,y),(x+w,y+h),(238,44,44),8)
	cv2.imshow("mog",fgmask)
	cv2.imshow("detection",frame)
	if cv2.waitKey(24) & 0xff == 27:
		break
camera.release()
cv2.destroyAllWindows()

