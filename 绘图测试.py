# 导入第三方库（pip可下载）
import matplotlib.pyplot
import numpy

# 导入自定义库
from dapas.statistics import *
from dapas.distribution import *


# 套壳函数（方便换函数）
def f(x):
    y = norm_s(x)  # 更换这里的函数即可
    # y = exp(x, 5)
    # y = unif(x, -1, 5)
    return y


# 生成数据与概率密度计算
X = numpy.linspace(-10, 10, 1000)
Y = []
for x_i in X:
    Y.append(f(x_i))


# 绘制图像
matplotlib.pyplot.figure(num=1, figsize=(10, 5))   # 第一张序号设置为0，后面的序号将从1开始
matplotlib.pyplot.plot(X, Y)


# 显示绘图结果
matplotlib.pyplot.show()