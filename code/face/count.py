import cv2 as cv


# 对每一帧图像进行人脸检测处理


def face_id(img, classifier):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray, 1.3, 5)
    count = 0
    if len(faces) == 0:
        cv.putText(img, str(count), (10, 100), cv.FONT_ITALIC, 4, (0, 0, 255))
        cv.imshow("1", img)
    else:
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count = count + 1
        cv.putText(img, str(count), (10, 100), cv.FONT_ITALIC, 4, (0, 0, 255))
        cv.imshow("1", img)


# 载入 Haar 检测器
face_cascade = cv.CascadeClassifier("./haarcascade_frontalface_alt.xml")
camera = cv.VideoCapture(0)
camera.set(cv.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv.CAP_PROP_FRAME_HEIGHT, 480)
camera.set(cv.CAP_PROP_FPS, 30)
cv.namedWindow("1")
while True:
    ret, frame = camera.read()
    face_id(frame, face_cascade)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyWindow("1")
camera.release()
