# 物体识别（OpenCV）

#### 分割和图像二值化

在本章中，我们着重于从图像中提取特征和物体。物体是我们处理的重点。这是我们真正想要做的事情，需要做进一步的工作。为了从图像中获取物体，我们需要经历一个称为分割的过程。可以通过多种不同方式进行分割，但是典型的输出是二进制图像。二进制图像是像素值为零或一的图像。本质上，1表示我们要使用的图像片段，0表示其他所有内容。

图像二值化是许多图像处理算法的关键组成部分。这些是纯黑白图像，仅提取您所需的结果。它们充当源图像区域的遮罩。从源创建二进制图像后，在图像处理方面您需要做很多事情。获取二进制图像的一种典型方法是使用所谓的阈值算法。这是一种细分类型，用于查看源图像的值并与一个人的中心值进行比较，以确定单个像素或一组像素的值应为零或一个。

#### 简单阈值

了解了分割和二进制图像的重要性之后，让我们看一下执行我们自己的简单阈值处理。

```python
import numpy as np
import cv2

bw = cv2.imread('detect_blob.png', 0)
height, width = bw.shape[0 : 2]
cv2.imshow("Original BW", bw)

binary = np.zeros([height, width, 1], 'uint8')

thresh = 85

for row in range(height):
    for col in range(width):
        if bw[row][col] > thresh: # 使用循环实现，像素值高于85的设为255，否则为0
            binary[row][col] = 255

cv2.imshow("Slow Binary", binary)

ret, thresh = cv2.threshold(bw, thresh, 255, cv2.THRESH_BINARY) # 使用opencv内置函数实现
cv2.imshow("CV Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

函数原型如下

```
cv2.threshold (源图片, 阈值, 填充色, 阈值类型)
```

1. **src**：源图片，必须是单通道

2. **thresh**：阈值，取值范围0～255

3. **maxval**：填充色，取值范围0～255

4. **type**：阈值类型，具体见下表

   | 阈值                                        | 小于阈值的像素点 | 大于阈值的像素点 |
   | ------------------------------------------- | ---------------- | ---------------- |
   | 0/cv2.THRESH_BINARY（黑白二值）             | 置0              | 置填充色         |
   | 1/cv2.THRESH_BINARY_INV（黑白二值反转）     | 置填充色         | 置0              |
   | 2/cv2.THRESH_TRUNC （得到的图像为多像素值） | 保持原色         | 置灰色           |
   | 3/cv2.THRESH_TOZERO                         | 置0              | 保持原色         |
   | 4/cv2.THRESH_TOZERO_INV                     | 保持原色         | 置0              |

尽管这是物体分割的一种非常简单的形式，并且在光照不均匀等情况下会失败，但它仍然广泛地适用。

#### 自适应阈值

尽管简单的阈值处理是一种强大的算法，但它也有其局限性，例如图像中光线不均匀时。这就是自适应阈值的适用场合。这是一种可以提高图像阈值操作的多功能性的技术。代替将简单的全局值用作阈值比较，自适应阈值处理将在图像的局部附近查找以确定是否满足相对阈值。这样，可以解决诸如照明不均匀的问题。

```python
import numpy as np
import cv2

img = cv2.imread('sudoku.png', 0)
cv2.imshow("Original", img)

ret, thresh_basic = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow("Basic Binary", thresh_basic)

thres_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Adaptive Threshold", thres_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

cv2.adaptiveThreshold的六个参数

- 第一个原始图像
- 第二个像素值上限
- 第三个自适应方法Adaptive Method:
  - cv2.ADAPTIVE_THRESH_MEAN_C ：领域内均值
  - cv2.ADAPTIVE_THRESH_GAUSSIAN_C ：领域内像素点加权和，权 重为一个高斯窗口
- 第四个值的赋值方法：只有cv2.THRESH_BINARY 和cv2.THRESH_BINARY_INV
- 第五个Block size:规定领域大小（一个正方形的领域）
- 第六个常数C，阈值等于均值或者加权值减去这个常数（为0相当于阈值 就是求得领域内均值或者加权值）

#### 皮肤探测

了解了不同的阈值类型后，我们可以应用从图像中检测和分割肤色的用例。如果没有单独的阈值会自行起作用，这还将涵盖使用复合过滤来改善结果。

```python
import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split HSV",hsv_split)

ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("Sat Filter", min_sat)

ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter", max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final", final)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindow()
```

进一步分解，我们可以看一下色相和饱和度过滤器。将最终图像放在最右边，我们可以看到色相滤镜实际上是如何与饱和度滤镜相乘以获得最终结果的。看看这是最有效的一个好例子是，如果我们先看最右边第二行，在这里的这个人，您会注意到在饱和滤镜中，右肩或左肩实际上是白色的，与色相滤镜中的黑色相同。

因此，在最后的过滤器中，它实际上已经消失了，将其隔离并得到和脸部更相似的特征。这是一个很好的例子，说明了如何使用多个过滤器进行阈值处理，从而获得更好的结果。最后，必须承认这不一定是检测面部的最可靠方法。更高级的技术将使用机器学习，或使用不被光线影响的方法。在这种情况下，我们使用的可能并非在所有环境中都适用的简单硬编码阈值。为了获得自己的结果或在其他图像上获得更好的结果，您可能需要调整这些参数。

#### 轮廓简介

分割图像的关键区域后，下一步通常是识别单个物体。但是，我们该怎么做呢？一种有效的方法是使用OpenCV的轮廓实现。轮廓的目标是输入二进制图像，并围绕场景中的所有单个物体创建紧密配合的封闭图形。周长称为轮廓。从数学的角度来看，它称为迭代能量减少算法。但是从概念上讲，我们可以将其视为一种弹性膜，该弹性膜从图像的边缘开始并挤压所有物体和形状。

它在所有这些物体周围创建边界。要注意的一件事是邻里和连通性的想法。轮廓将把大于零的任何像素值视为前景的一部分，并且将其他与该像素接触或连接的其他像素视为同一物体的一部分。在算法运行时，它将尝试减少所有这些物体的能量或边界框，直到得出收敛的结果。重要的是要理解，尽管这可能是一个迭代算法，但我们知道轮廓总是会收敛的，因此它永远不会陷入无限循环中。

最后，您有一个轮廓列表，每个轮廓只是一个线性的点列表，这些点描述了单个物体的周长。它们始终是封闭的，这是一个技术术语，表示没有间隙。这意味着可以将它们安全地拉回到图像上并完全填充新的颜色。 轮廓是确定关于图像中单个物体的许多其他有用属性的基础技术之一，这使其成为我们图像处理中非常强大的算法。它从通常通过阈值过滤完成的物体分割转移到物体检测。

#### 轮廓物体探测

现在我们已经了解了轮廓的工作原理，让我们看看如何在OpenCV中使用它们。

```python
import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)

cv2.drawContours(img2, contours, index, color, thickness)
cv2.imshow("Contours", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

需要注意的是cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图），所以读取的图像要先转成灰度的，再转成二值图。

findContours函数原型

```
cv2.findContours(image, mode, method[, contours[, hierarchy[, offset ]]])  
```

- 第一个参数是寻找轮廓的图像；
- 第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
  - cv2.RETR_EXTERNAL表示只检测外轮廓
  - cv2.RETR_LIST检测的轮廓不建立等级关系
  - cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
  - cv2.RETR_TREE建立一个等级树结构的轮廓。
- 第三个参数method为轮廓的近似办法
  - cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
  - cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
  - cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法

cv2.findContours()函数返回两个值，一个是轮廓本身，还有一个是每条轮廓对应的属性。

drawContours函数原型

```
cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset ]]]]])  
```

- 第一个参数是指明在哪幅图像上绘制轮廓；
- 第二个参数是轮廓本身，在Python中是一个list。
- 第三个参数指定绘制轮廓list中的哪条轮廓，如果是-1，则绘制其中的所有轮廓。后面的参数很简单。其中thickness表明轮廓线的宽度，如果是-1（cv2.FILLED），则为填充模式。绘制参数将在以后独立详细介绍。

#### 面积，周长，中心和曲率

现在，我们已经在上节中分割了物体的轮廓并对其进行了单独限制，让我们继续进行下去，并从每个单独的物体中提取更多信息。具体来说，我们将研究这些物体的面积，周长和质心。

```python
import numpy as np
import cv2

img = cv2.imread('detect_blob.png',1)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow("Binary", thresh)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img2 = img.copy()
index = -1
thickness = 4
color = (255, 0, 255)

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')
for c in contours:
    cv2.drawContours(objects, [c], -1, color, -1)

    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)

    M = cv2.moments(c)
    cx = int( M['m10'] / M['m00'] )
    cy = int( M['m01'] / M['m00'] )
    cv2.circle(objects, (cx, cy), 4, (0, 0, 255), -1)

    print("Area: {}, perimeter: {}".format(area, perimeter))

cv2.imshow("Contours", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

cv2.contourArea()函数可以计算面积

cv2.arcLength()计算周长，第二个参数表示轮廓是闭合（True）还是打开的

cv2.moments()会计算图像的矩，并返回一个字典

#### Canny边缘检测算法

通常，我们需要对图像进行预处理以改善最终结果，并且在从图像中的各个物体提取轮廓的情况下，通常很容易先检测并加深图像中的边缘。 Canny边缘检测算法是一种边缘检测算法，可以很好地帮助在图像中创建更好的物体分离效果。一般来说，边缘检测算法着眼于图像上颜色变化的速率或速度。 Canny边缘检测算法是该算法的一种特定形式，可在图像的关键高梯度区域创建一条像素宽的线。

如果在我们的分割过程中存在重叠，这可以帮助分解物体。让我们看一下如何使用Canny边缘检测算法。

```python
import numpy as np
import cv2

img = cv2.imread("tomatoes.jpg",1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
res, thresh = cv2.threshold(hsv[:, :, 0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("thresh", thresh)

edges = cv2.Canny(img, 100, 70)
cv2.imshow("Canny", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

Canny函数的原型

```
cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]]) 
```

必要参数：

- 第一个参数是需要处理的原图像，该图像必须为单通道的灰度图
- 第二个参数是阈值1
- 第三个参数是阈值2

函数返回一副二值图，其中包含检测出的边缘。

#### 物体探测概览

在本章中，我们回顾了几种方法来分割图像中的物体并检测这些物体的属性。我们研究了几个领域，包括使用边缘的简单和自适应阈值处理，以帮助分解紧密匹配的物体。我们还简要介绍了如何将不同类型的多个阈值组合在一起，并且在上一章中，我们了解了如何使用高斯模糊来减少噪声，如何使用膨胀和腐蚀过滤器来减少小斑点或间隙。这些只是一些有助于分割物体的图像处理工具。

牢记上下文非常重要。知道应用程序将用于什么，并开发适合用例的细分。您是否知道对于不同的图像输入，您的照明将始终保持大致相同？如果这样，使用非自适应阈值可能更有效；也许您可以通过收集自己的全球平均值或均值来提高阈值。物体的方向和比例如何？您可以假设图像中物体的大小，从而过滤掉不适合该大小的任何内容吗？此外，它是实时应用程序吗？帧之间的一致性可能非常重要？至于过滤，是否对结果进行过度过滤或过滤不足？例如，如果检测到一个物体触发了诸如发送电子邮件之类的操作，那么您可能希望对没有误报更加敏感。

尽管本课程仅涵盖识别和表征图像物体的几种基本方法，但是还有许多其他应用程序和高级技术可以将图像或序列中的物体进行分割。在上一段中，我们谈到了物体检测的先验方法。这意味着需要事先了解有关上下文或输入的信息。例如，如果您知道图像的主题将始终是黑色背景，则可以进行不同的假设和处理技术决策，而在一般情况下是不会的。当试图检测和分割图像中的物体时，请注意所有可用的工具。

知道环境的参数将如何变化，并考虑如何将流程分解为更小的步骤。