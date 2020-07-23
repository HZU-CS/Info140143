"""
基于百度云服务的人脸识别
"""


import base64
import requests
import cv2

# client_id 为官网获取的App Key， client_secret为官网获取的Secret Key
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
       '&client_secret='
# 请求Access Token
res = eval(requests.get(host).text)
token = res['access_token']
if token:
    print(token)

access_token = token
# 人脸识别云服务接口
url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect?access_token=' + access_token
header = {
    'Content-Type': 'application/json'
}
# 二进制只读模式打开文件
filename = r'face.jpg'

with open(filename, 'rb') as f:
    # 图像转换为Base64格式
    img = base64.b64encode(f.read())

origin = cv2.imread(filename)

params = {'image': img,
          'image_type': "BASE64",
          'max_face_num': 10,
          'face_field': 'faceshape,facetype'}
# 提交请求并解析返回数据
res2 = eval(requests.post(url=url, data=params, headers=header).text)

# 人脸数量
face_num = res2['result']['face_num']
# 人脸列表
face_list = res2['result']['face_list']
# 人脸位置
face_location = [item['location']
                 for item in face_list if item['face_type']['type'] == 'human']

for loc in face_location:
    # 每个人脸绘制矩形框
    cv2.rectangle(origin, (int(loc["left"]), int(loc["top"])),
                  (int(loc["left"] + loc["width"]), int(loc["top"] + loc["height"])), (255, 0, 0), 2)

# 绘制文本
cv2.putText(origin, 'num: {}'.format(face_num), (0, 15),
            cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

# 显示
cv2.imshow('face detector', origin)
# 输出图片
cv2.imwrite('face_detect.png', origin)
cv2.waitKey(0)
cv2.destroyAllWindows()
