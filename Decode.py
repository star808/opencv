import cv2
import numpy as np
#二维码图片
img=cv2.imread('python.png')
#初始化CV2的二维码检测器
decoder = cv2.QRCodeDetector();

#解码
retval,points,straight_qrcode = decoder.detectAndDecode(img)
#如果解码成功
'''
if bbox is not None:
    print(f"QRCode data:\n{data}")
    #用线条显示图像
    #边框长度
    n_lines = len(bbox)
    for i in range (n_lines):
        #输出
        point1 = tuple(bbox[i][0])
        point2=tuple(bbox[(i+1)%n_lines][0])
        cv2.line(img,point1,point2,color=(255,0,0),thickness=2)
'''

if retval:
    print(retval)
    #points_int =[]
    #for point in points:
    #   points_int.append([int(p) for p in point])
    points_int = np.array(points).reshape(-1, 1, 2).astype(np.int32)
    cv2.polylines(img,[points_int],True,(0,255,0),5)
    cv2.putText(img,retval,(points_int[0][0][0],points_int[0][0][1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2)
#显示结果

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

