
import cv2
import numpy as np
import time
import datetime

a = datetime.datetime.now().strftime('%S%f')
camera = cv2.VideoCapture("6号B.mp4")
mog = cv2.createBackgroundSubtractorMOG2()
ret, frame = camera.read()
b = datetime.datetime.now().strftime('%S%f')
ccc = int(b[0:2]) - int(a[0:2])
eee = int(b[2:4]) - int(a[2:4])
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = camera.get(cv2.CAP_PROP_FPS)
size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), \
                                            int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('camera_test.avi', fourcc, fps, size)
while (ccc < 5) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (eee < 7) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (ccc < 9) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (eee < 14) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (ccc < 16) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (eee < 8) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (ccc < 19) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (eee < 16) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (ccc < 24) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while (eee < 15) :
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
while True:
    print(ccc)
    b = datetime.datetime.now().strftime('%S%f')
    ccc = int(b[0:2]) - int(a[0:2])
    eee = int(b[2:4]) - int(a[2:4])
    ret, frame = camera.read()
    fgmask = mog.apply(frame)
    blur = cv2.medianBlur(fgmask, 5)  # 中值滤波
    th2 = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY)[1]  # 阈值处理
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    eroded_2 = cv2.erode(th2, kernel, iterations=3)
    eroded_1 = cv2.erode(th2, kernel, iterations=1)
    dilated = cv2.dilate(eroded_2, kernel, iterations=11)
    image, contours, gihr = cv2.findContours(dilated, cv2.RETR_EXTERNAL,
                                             cv2.CHAIN_APPROX_SIMPLE)  # 提取图像轮廓。参数1：图像，参数2：提取规则cv2.RETR_EXTERNAL：只找外轮廓，cv2.RETR_TREE：内外轮廓都找。
    # 参数3：输出轮廓内容格式。cv2.CHAIN_APPROX_SIMPLE：输出少量轮廓点。cv2.CHAIN_APPROX_NONE：输出大量轮廓点。
    # 计算轮廓的边界框，并加在图片上                                                             #输出参数1：图像。输出参数2：轮廓列表。输出参数3：层级
    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255),8)
    # 腐蚀
    #cv2.imshow("eroded_1", eroded_1)
    cv2.imshow("dilated", dilated)
    #cv2.imshow("detection", frame)
    line1 = np.array([[0,0],
                      [231, 289]]).reshape((-1, 1, 2))
    line2 = np.array([[231, 289],
                      [231-10, 289+40]]).reshape((-1, 1, 2))
    line3 = np.array([[[ 231+220 , 289]],
                      [[231, 289]]]).reshape((-1, 1, 2))
    line4 = np.array([[[ 231+220, 289]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    line5 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [ line2, line3,line4,line5], True, (0, 255, 255),4)
    line6 = np.array([[[231-10, 289+40]],
                      [[231+220+110, 289+45]]])
    line7 = np.array([[[231-10, 289+40]],
       [[ 231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    line8 = np.array([[[231+220+110, 289+45]],
       [[231+220+110+130, 289+45+60]]]).reshape((-1, 1, 2))
    line9 = np.array([[[231+220+110+130, 289+45+60]],
       [[231+220+110+130, 289+45+60+60]]]).reshape((-1, 1, 2))
    line10 = np.array([[[231+220+110+130, 289+45+60+60]],
       [[231-10+46, 289+40+131]]]).reshape((-1, 1, 2))
    cv2.polylines(frame, [line6 , line7, line8, line9, line10], True, (0, 0, 255),4)
    cv2.putText(frame,"Early-warning Zone",(250,320),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1)
    cv2.putText(frame,"Alarm Zone",(250,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("video",frame)
    out.write(frame)
    if cv2.waitKey(24) & 0xff == 27:
        break
camera.release()
cv2.destroyAllWindows()

#适合车辆较少的场景
#识别靠近摄像头的车辆行人
#根据区域中心判断所在区域
