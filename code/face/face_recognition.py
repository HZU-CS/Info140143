import glob
import face_recognition
import numpy as np
import os
import cv2 as cv


def face_recog():
    # 读取注册的人脸特征 npy 文件
    feature_path = os.path.join("files", "*.npy")
    feature_files = glob.glob(feature_path)
    # 解析文件名称，作为注册人姓名
    feature_names = [item.split(os.sep)[-1].replace(".npy", "")
                     for item in feature_files]
    # print(feature_names)
    cap = cv.VideoCapture(0)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
    features = []
    for f in feature_files:
        feature = np.load(f)
        features.append(feature)
    while True:
        ret, frame = cap.read()
        # 视频流中人脸特征编码
        img_encoding = face_recognition.face_encodings(frame)
        flag = False
        if len(img_encoding) != 0:
            # 获取人脸特征编码
            img_encoding = face_recognition.face_encodings(frame)[0]
            # 与注册的人脸特征进行对比
            result = face_recognition.compare_faces(
                features, img_encoding, tolerance=0.4)
            count = 0
            for i in result:
                if i:
                    flag = True
                    break
                count = count + 1
        cv.imshow("result", frame)
        # 主动跳出
        key = cv.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        if flag:
            break

    cap.release()
    cv.destroyAllWindows()
    if feature_names:
        return flag, feature_names[count]
    else:
        return flag, feature_names


if __name__ == '__main__':
    f, name = face_recog()
    if f:
        print("人脸识别通过，姓名:{}".format(name))
    else:
        print("人脸识别失败")
