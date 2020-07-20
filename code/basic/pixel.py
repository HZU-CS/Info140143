import cv2

img = cv2.imread("opencv-logo.png", 1)  # 第2个参数是1表示使用图像的默认颜色和色彩通道，如果是0则表示以黑白形式读入该图片

print(img)  # 会发现是一个数组
print(type(img))  # 类型是<class 'numpy.ndarray'>

print(len(img))  # 表示数组的行
print(len(img[0]))  # 表示数组的列
print(len(img[0][0]))  # 表示通道数，这里是3，表示RGB红绿蓝3通道

print(img.shape)  # 直接打印出这3项参数
print(img.dtype)  # uint8，数据类型是8bit的无符号整数，也就是色彩从0~255

print(img[10, 5])  # 第10行第5列的像素，是一个有3个数的一维数组
print(img[:, :, 0])  # 打印出第一个通道的所有数据，即R通道在每个点上的数据

print(img.size)  # 像素的个数
