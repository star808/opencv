# 1 导入库
import cv2
import argparse

# 2 获取参数
parser = argparse.ArgumentParser()

#3 添加参数
parser.add_argument("video_path",help="path to save file")

#4 解析参数
args = parser.parse_args()

#5 捕获摄像头
capture= cv2.VideoCapture(0)

#6 是否打开了摄像头
if capture.isOpened() is False:
    print("Open Camera Error")

# 7 获取帧的属性： 宽 高 fps
frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_heigt = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)


#8 对视频进行编码
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output_gray = cv2.VideoWriter(args.video_path,fourcc,int(fps),(int(frame_width),int(frame_heigt)),False)

# 9 读取摄像头
while capture.isOpened():
    ret,frame = capture.read() # 一帧一帧地读取
    if ret is True:
        # 10 将读取到的帧转换为灰度
        gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGRA2GRAY)
        # 11 将转化后的帧写入到新的视频文件中
        output_gray.write(gray_frame)
        # 12 显示视频
        cv2.imshow("gray",gray_frame)
        # 等待退出
        cv2.waitKey(0) & 0xFF ==ord('q')
        break
    else:
        break

capture.release()
output_gray.release()
cv2.destroyAllWindows()











