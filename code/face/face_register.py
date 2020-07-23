import argparse

import face_recognition
import numpy as np
import os
import cv2 as cv


def face_register():
    flag = False
    print("获取人脸中")
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv.CAP_PROP_FPS, 30)
    while True:
        ret, image = cap.read()
        key = cv.waitKey(1) & 0xFF
        # 如果按下键盘的"g"字符，则开始保存人脸
        if key == ord("g"):
            image_encoding = face_recognition.face_encodings(image)[0]
            if len(image_encoding) != 0:
                flag = True
                break
            else:
                print("没有检测到人脸")
        elif key == 27:
            break
        cv.imshow("face_register", image)
    cap.release()
    cv.destroyAllWindows()
    return image_encoding, flag


ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True, help="请输入注册人的姓名：")
args = vars(ap.parse_args())
image_encoding, flag = face_register()
if flag:
    feature_name = args["name"] + ".npy"
    feature_path = os.path.join("./files", feature_name)
    np.save(feature_path, image_encoding)
    print("已保存人脸")
