"""
基于百度云服务的车型识别
"""

import base64
import requests
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# client_id 为官网获取的App Key， client_secret为官网获取的Secret Key
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
       '&client_secret='
# 请求Access Token
res = eval(requests.get(host).text)
token = res['access_token']
if token:
    print(token)

access_token = token
# 车型识别云服务接口
url = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car?access_token=' + access_token
header = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
# 二进制只读模式打开文件
filename = r'car.png'

with open(filename, 'rb') as f:
    # 图像转换为Base64格式
    img = base64.b64encode(f.read())
# f = open(filename, 'rb')
origin = cv2.imread(filename)

# image: base64图像
params = {"image": str(img, 'utf-8')}
# 提交请求并解析返回数据
res2 = eval(requests.post(url=url, data=params, headers=header).text)

# 获取车型识别结果在图像中的位置
loc = res2['location_result']

# 绘制矩形外框
cv2.rectangle(origin, (int(loc["left"]), int(loc["top"])),
              (int(loc["left"]) + int(loc["width"]), int(loc["top"]) + int(loc["height"])), (255, 0, 0), 2)

# 设置字体
font_size = 30
font_hei = ImageFont.truetype("./simhei.ttf", font_size, encoding="utf-8")
# 图像色彩格式转换
img_rgb = cv2.cvtColor(origin, cv2.COLOR_BGR2RGB)
# 使用PIL读取图像像素数组
pilimg = Image.fromarray(img_rgb)

# 绘制图像
draw = ImageDraw.Draw(pilimg)
# 车型识别置信度
car_score = res2['result'][0]['score']
# 车型名称
car_name = res2['result'][0]['name']
# 绘制字符
draw.text((loc["left"], loc["top"]), car_name + '  ' +
          str(car_score), (255, 0, 0), font=font_hei)

origin = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

# 显示
cv2.imshow('word detector', origin)
# 输出图片
cv2.imwrite('car_rec.png', origin)
cv2.waitKey(0)
cv2.destroyAllWindows()
