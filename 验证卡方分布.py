# 【导入库】
# 导入第三方库
import matplotlib.pyplot
import numpy
# 导入自定义库
from dapas.statistics import *
from dapas.distribution import *


# 【生成数据与概率密度计算】
N = 10000
X = numpy.linspace(0, 40, N)
S = []
S = sample(N)

# 卡方分布
Y = []
for x_i in X:
    Y.append(chisq(x_i, 4))

#
X_1 = []
for x_i in X:
    X_1.append(norm(x_i))
X_2 = []
for x_i in X:
    X_2.append(norm(x_i))
X_3 = []
for x_i in X:
    X_3.append(norm(x_i))
X_4 = []
for x_i in X:
    X_4.append(norm(x_i))


Y_0 = []
i = 0
while(i < N):
    Y_0.append(X_1[i]**2 + X_2[i]**2 + X_3[i]**2 + X_4[i]**2)
    i = i+1
# print(Y_0)

Y_1 = []
for x_i in X:
    Y_1.append(chisq(x_i, 1))
Y_2 = []
for x_i in X:
    Y_2.append(chisq(x_i, 4))
Y_3 = []
for x_i in X:
    Y_3.append(chisq(x_i, 10))
Y_4 = []
for x_i in X:
    Y_4.append(chisq(x_i, 20))


# 【绘制图像】
# 图1：验证
matplotlib.pyplot.figure(num=1, figsize=(10, 5))
matplotlib.pyplot.plot(X, Y, color="red", linewidth=1)
matplotlib.pyplot.plot(X, Y_0, color="blue", linewidth=1)

# 图2：验证
matplotlib.pyplot.figure(num=2, figsize=(10, 5))
matplotlib.pyplot.plot(X, Y_1, color="red", linewidth=1, linestyle="--")
matplotlib.pyplot.plot(X, Y_2, color="blue", linewidth=1, linestyle="--")
matplotlib.pyplot.plot(X, Y_3, color="green", linewidth=1, linestyle="--")
matplotlib.pyplot.plot(X, Y_4, color="black", linewidth=1, linestyle="--")
# 设置 x、y 轴显示数据的区间
matplotlib.pyplot.xlim(0, 40)
matplotlib.pyplot.ylim(0, 0.2)

# 显示绘图结果
matplotlib.pyplot.show()
