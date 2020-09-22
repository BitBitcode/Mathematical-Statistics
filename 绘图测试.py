# 导入第三方库（pip可下载）
import matplotlib.pyplot
import numpy

# 导入自定义库
from dapas.statistics import *
from dapas.distribution import *


# 套壳函数（方便换函数）
def f(x):
    y = norm(x)  # 更换这里的函数即可
    # y = exp(x, 5)
    # y = unif(x, -1, 5)
    return y


# 生成数据与概率密度计算
X = numpy.linspace(-20, 20, 100000)
Y_1 = []
for x_i in X:
    Y_1.append(f(x_i))
Y_2 = []
for x_i in X:
    Y_2.append(tdis(x_i, 5))


# 绘制图像
matplotlib.pyplot.figure(num=1, figsize=(10, 5))   # 第一张序号设置为0，后面的序号将从1开始
matplotlib.pyplot.plot(X, Y_1, color="red")
matplotlib.pyplot.plot(X, Y_2, color="blue")


# 显示绘图结果
matplotlib.pyplot.show()