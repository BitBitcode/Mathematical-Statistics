# 【库说明】
"""
【数理统计系列库】

简介
+ 库名：distribution.py
+ 功能：概率密度函数与分布函数

库函数
+ f_uniformity(a, b, x)
+ f_exponent(k, x)
+ f_norm(m, s, x):
+ f_norm_s(x)

更多信息
+ 作者：Kiana Kaslana
+ 个人邮箱：smilewwc@qq.com
+ 个人网页：https://bitbitcode.github.io/
+ 开源地址：https://gitee.com/Acrylic-Studio/Mathematical-Statistics

更新日志
+ 创建日期：2020.9.20

Copyright (c) BitBitcode. All rights reserved.
"""


# 【导入库】
# 第三方库
import math
# 自定义库
import statistics
from dapas.toolfunction import *


# 【概率密度函数】
# 均匀分布
def unif(a, b, x):
    """
    【函数说明】

    功能：均匀分布的概率密度函数（Uniformity）

    参数：
    + a：[浮点数] 区间左端点的横坐标值
    + b：[浮点数] 区间右端点的横坐标值
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    if (a < x < b):
        y = 1 / (b - a)
        return y
    else:
        return 0


# 指数分布
def exp(x, k):
    """
    【函数说明】

    功能：指数分布的概率密度函数（Exponent）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值
    + k：[浮点数] 指数分布的参数

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    if (x > 0):
        y = k * math.exp(- k * x)
        return y
    else:
        return 0


# 二项分布
def binom(x, p, n=1):
    """
    【函数说明】

    功能：二项分布的概率密度函数（Binomial Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值
    + n：[整数] 试验次数
    + p: [浮点数] 概率

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    y = C(n, x) * (p**x) * ((1-p)**(n-x))
    return y


# 泊松分布
def pois(x, Lambda):
    """
    【函数说明】

    功能：泊松分布的概率密度函数（Poison Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值
    + Lambda：[浮点数] 泊松分布的参数（λ）

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    k = 0   # 这里有问题
    y = ((Lambda**k)*math.exp(-Lambda))/(fac(k))
    return y


# 几何分布
def geom(x):
    """
    【函数说明】

    功能：二项分布的概率密度函数（Geometry Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    pass


# 正态分布
def norm(x, Mu, Sigma):
    """
    【函数说明】

    功能：一般正态分布的概率密度函数（Normal）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值
    + Mu：总体的期望（μ）
    + Sigma：总体的方差（σ） 

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    y = (1/((math.sqrt(2*math.pi))*Sigma)) * math.exp(-((x-Mu)**2)/(2*Sigma**2))
    return y


# 标准正态分布
def norm_s(x):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（Standard Normal），样本期望为0，样本方差为1

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    y = (1/math.sqrt(2*math.pi)) * math.exp(-(x**2)/2)
    return y


# Γ分布
def gamma(x):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（Gamma Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    pass

# t分布


def tdis(x):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（t Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    pass


# F分布
def fdis(x):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（F Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    pass


# β分布
def beta(x):
    """
    【函数说明】

    功能：β分布的概率密度函数（t Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    pass


# Χ^2分布
def chisq(x):
    """
    【函数说明】

    功能：卡方分布的概率密度函数（Χ^2 Distribution）

    参数：
    + x：[浮点数] 某个样本点（x）的横坐标值

    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    pass


# 【模块内测试代码】
if __name__ == "__main__":
    X_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in X_series:
        print("X~U(0,1)", x, "：", unif(1, 5, x))
        print("X~E(0,1)", x, "：", exp(5, x))
