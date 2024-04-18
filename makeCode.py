#https://www.zhihu.com/tardis/zm/art/186013877?source_id=1005


import qrcode

data = "371526"

filename = "python.png"

img = qrcode.make(data)

img.save(filename)