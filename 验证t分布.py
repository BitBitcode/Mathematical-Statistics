# 【导入库】
# 导入第三方库
import matplotlib.pyplot
import numpy
# 导入自定义库
from dapas.statistics import *
from dapas.distribution import *


# 【生成数据与概率密度计算】
X = numpy.linspace(-20, 20, 200000)

# 正态分布
Y_1 = []
for x_i in X:
    Y_1.append(norm(x_i))

# t分布
Y_2 = []
for x_i in X:
    Y_2.append(tdis(x_i, 5))


# 【绘制图像】
# 图1：验证t分布在大样本的情况下区域正态分布
matplotlib.pyplot.figure(num=1, figsize=(10, 5))

matplotlib.pyplot.plot(X, Y_1, color="red", linewidth=1, linestyle="--")
matplotlib.pyplot.plot(X, Y_2, color="blue", linewidth=1)

# 设置 x、y 轴显示数据的区间
# matplotlib.pyplot.xlim(-20, 20)
# matplotlib.pyplot.ylim(-0.1, 0.5)

# 显示绘图结果
matplotlib.pyplot.show()