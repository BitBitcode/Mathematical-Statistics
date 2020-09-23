# 导入第三方库（pip可下载）
import matplotlib.pyplot
import numpy

# 导入自定义库
from dapas.statistics import *
from dapas.distribution import *


# 套壳函数（方便换函数）
def f(x):
    y = binom(x, 0.2, 20)     # 更换这里的函数即可
    #y = pois(x, )
    return y


# 生成数据与概率密度计算
X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Y_1 = []
for x_i in X:
    Y_1.append(f(x_i))


# 绘制图像
matplotlib.pyplot.figure(num=1, figsize=(10, 5))   # 第一张序号设置为0，后面的序号将从1开始
# matplotlib.pyplot.scatter(X, Y_1, color="blue")   # 散点图
matplotlib.pyplot.bar(X, Y_1, width=0.5, color="blue", label="Binomial Distribution (p=0.2, n=20)")   # 条形图


# 显示图例
matplotlib.pyplot.legend(loc="upper right")


# 显示绘图结果
matplotlib.pyplot.show()
