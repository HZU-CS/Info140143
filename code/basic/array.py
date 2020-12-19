import numpy as np
import cv2

# 全黑色图片
# 0 ~ 255
black = np.zeros([150, 200, 1], 'uint8')  # 所有通道都是0，显示黑色
cv2.imshow("Black", black)
print(black[0, 0, :])

# 几乎黑色图片
ones = np.ones([150, 200, 3], 'uint8')
cv2.imshow("Ones", ones)
print(ones[0, 0, :])

# 全白色图片
white = np.ones([150, 200, 3], 'uint16')
white *= (2 ** 16 - 1)  # 点乘，所有通道都是最高，显示白色
cv2.imshow("White", white)
print(white[0, 0, :])

# 全蓝色图片
color = ones.copy()  # 深拷贝
color[:, :] = (255, 0, 0)  # 蓝色通道最高，其余通道为0，显示蓝色
cv2.imshow("Blue", color)
print(color[0, 0, :])

cv2.waitKey(0)
