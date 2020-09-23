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
X = numpy.linspace(-10, 10, 100)
Y = []
for x_i in X:
    Y.append(f(x_i))
Y_1 = []
for x_i in X:
    Y_1.append(norm(x_i, 0, 0.8))
Y_2 = []
for x_i in X:
    Y_2.append(norm(x_i, 0, 2))
Y_3 = []
for x_i in X:
    Y_3.append(norm(x_i, 0, 4))
Y_4 = []
for x_i in X:
    Y_4.append(norm(x_i, 0, 8))


# 绘制图像
matplotlib.pyplot.figure(num=1, figsize=(10, 5))   # 第一张序号设置为0，后面的序号将从1开始
INS_line0, = matplotlib.pyplot.plot(X, Y, color="black", linewidth=1, linestyle="--", label="σ = 0.8")
INS_line1, = matplotlib.pyplot.plot(X, Y_1, color="red", linewidth=1, linestyle="-", label="σ = Standard")
INS_line2, = matplotlib.pyplot.plot(X, Y_2, color="blue", linewidth=1, linestyle="-", label="σ = 2")
INS_line3, = matplotlib.pyplot.plot(X, Y_3, color="green", linewidth=1, linestyle="-", label="σ = 4")
INS_line4, = matplotlib.pyplot.plot(X, Y_4, color="orange", linewidth=1, linestyle="-", label="σ = 8")


# 显示图例
matplotlib.pyplot.legend(loc="upper right")
# matplotlib.pyplot.legend(handles=[INS_line1, INS_line0, INS_line2, INS_line3, INS_line4], labels=["σ = 0.8", "Standard", "σ = 2", "σ = 4", "σ = 8"])
# handles: 设置显示哪些曲线的图例
# labels(标签): 这里设置的文字将会覆盖绘图中设置的标签文字
# loc(位置): best（系统根据窗口大小以及图线占据的位置自动调整）, upper right, center right, lower right


# 显示绘图结果
matplotlib.pyplot.show()
