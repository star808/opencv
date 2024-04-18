#https://www.zhihu.com/tardis/zm/art/186013877?source_id=1005
#使用qrcode  生成二维码图片，保存在当前目录下
import cv2
import qrcode

#需要生成的数据
data = "www.cn.bing.com"

#生成的文件名
filename = "python.png"

#生成图片
img = qrcode.make(data)
#保存图片
img.save(filename)

#显示图片
mat_img=cv2.imread("python.png",cv2.COLOR_BGRA2GRAY)
cv2.imshow("img_window",mat_img)
cv2.waitKey(0)

