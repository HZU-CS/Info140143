# 人脸识别（OpenCV） 

#### 参考

> [十行Python代码实现人脸识别](https://zhuanlan.zhihu.com/p/66368987)
>
> [face recogntion官方文档](https://github.com/ageitgey/face_recognition/blob/master/README_Simplified_Chinese.md)

## 人脸检测

1. 提取特征
2. 训练
3. 级联检测

detection.py

count.py

## 人脸识别

### face_recognition

face_recognition 库是一个强大、简单、易上手的人脸识别开源项目，并且配备了完整的开发文档和应用案例，特别是兼容树莓派系统。项目 README 文件已经被翻译成中文，此项目是世界上最简洁的人脸识别库，你可以使用 Python 和命令行工具提取、识别、操作人脸。同时此项目的人脸识别是基于业内领先的 C++开源库 dlib 中的深度学习模型，用 Labeled Faces in the Wild 人脸数据集进行测试，有高达99.38%的准确率。 face_recognition.face_encodings 函数会调用 shape_predictor_68_face_landmarks.dat 识别出人脸的 68 个特征点位置，最后返回一个 128 维的向量,不过这个过程仅仅是一个粗定位的过程。如果想要精细的定位，可以调用 face_recognition.face_landmark 函数，该函数会返回一个列表，其中每个元素都包含嘴唇、眉毛、鼻子等精细区域的特征点的位置。

本实验使用 face_recognition 库的主要函数包括：

人脸对比函数

人脸编码距离函数

人脸特征编码函数

#### 环境准备

在Windows平台没有安装过visual studio2015版本或者更新以及MSVC版本没有达到2015版本或者更新的同学。

1. 先去Visual Studio2019官网下载

   [Visual Studio 2019 IDE - 适用于 Windows 的编程软件 (microsoft.com)](https://visualstudio.microsoft.com/zh-hans/vs/)

   ![vs](./vs.png)

2. 下载后打开会安装installer

3. installer中选择Visual Studio Community 2019安装并且选择使用 C++的桌面开发

   ![installer](./installer.png)

   ![C++](./C++.png)

4. 下载完成后即可进行下面的操作

安装cmake

```powershell
pip install cmake
```

安装argparse

```powershell
pip install argparse
```

安装face_recognition 

```powershell
pip install face-recognition
```

人脸注册

face_register.py

人脸识别

face_recognition.py