import cv2

img = cv2.imread("opencv-logo.png") # 用OpenCV读取opencv-logo.png图片并保存到变量img中
cv2.namedWindow("Image", cv2.WINDOW_NORMAL) # 给显示图片的窗口命名，并且采用默认模式
cv2.imshow("Image", img) # 展示图片

cv2.waitKey(0) # 等待用户按键

cv2.imwrite("output.jpg", img) # 将图片内容写入到output.jpg中