

import cv2
import numpy as np
import argparse
decoder = cv2.QRCodeDetector()
#创建一个VideoCapture对象，参数可以是设备索引号，或者视频文件的路径
#如果参数是0，它将尝试打开默认的摄像头

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("无法打开摄像头")

frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

print("Frame width:{}".format(frame_width))
print("Frame height:{}".format(frame_height))
print("Frames per second:{}:".format(fps))

while True:
    #从摄像头捕获一帧视频
    ret,img = cap.read()
    #如果帧读取正确，则显示视频帧
    if ret:
        #cv2.imshow("v",img)
        gray_img=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
        retval,points,straight_qrcode =decoder.detectAndDecode(gray_img)
        if retval:
            print(retval)
            # points_int =[]
            # for point in points:
            #   points_int.append([int(p) for p in point])
            points_int = np.array(points).reshape(-1, 1, 2).astype(np.int32)
            cv2.polylines(gray_img, [points_int], True, (0, 255, 0), 5)
            cv2.putText(img, retval, (points_int[0][0][0], points_int[0][0][1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9,
                        (255, 0, 0), 2)
        cv2.imshow("v",gray_img)
    #按q 键退出循环
    if cv2.waitKey(1)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

