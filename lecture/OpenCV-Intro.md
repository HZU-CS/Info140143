# 基础图像识别（OpenCV）

![OpenCV官方文档](https://atts.w3cschool.cn/attachments/cover/opencv.gif?t=1314520&imageView2/1/w/150/h/84)

OpenCV（开源计算机视觉库）是一个开源的BSD许可库，其中包含数百种计算机视觉算法。本节课主要介绍OpenCV 2.x API，它本质上是一个C ++ API，与基于C的OpenCV 1.x API相反。

## OpenCV简介

OpenCV 是 Intel 开源计算机视觉库。它由一系列 C 函数和少量 C++ 类构成，实现了图像处理和计算机视觉方面的很多通用算法。

OpenCV 拥有包括 300 多个C函数的跨平台的中、高层 API。它不依赖于其它的外部库——尽管也可以使用某些外部库。

OpenCV 对非商业应用和商业应用都是免费（FREE）的。（细节参考 license）。

## OpenCV特点

- 跨平台:[Windows](https://www.w3cschool.cn/windowsappbook/)、[Linux](https://www.w3cschool.cn/linux/)、[Android](https://www.w3cschool.cn/uawnhh/)
- 开源免费，无论商业与否
- 高效快速，使用方便

## OpenCV下载安装

推荐使用已编译的非官方库，如果安装过慢推荐使用国内的源，在Windows和Mac系统下

安装numpy库

```powershell
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple
```

安装opencv库

```powershell
pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
```

除了清华大学的源以外，还可以使用以下源

> http://mirrors.aliyun.com/pypi/simple/ //阿里
>
> http://pypi.douban.com/ //豆瓣
>
> http://pypi.hustunique.com/ //华中理工大学
>
> http://pypi.sdutlinux.org/ //山东理工大学
>
> http://pypi.mirrors.ustc.edu.cn/ //中国科学技术大学

Linux系统下将pip改为pip3。

下载完成后输入以下Python代码检查

```python
import cv2
print(cv2.__version__)
```

能打印出版本号则说明安装正常。

