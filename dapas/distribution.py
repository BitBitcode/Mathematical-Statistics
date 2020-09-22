# 【库说明】
"""
数理统计系列库
============

简介
-------
+ 库名：dapas.distribution.py
+ 功能：概率密度函数与分布函数

库函数
-------
+ f_uniformity(a, b, x)
+ f_exponent(k, x)
+ f_norm(m, s, x):
+ f_norm_s(x)

更多信息
-------
+ 作者：Kiana Kaslana
+ 个人邮箱：smilewwc@qq.com
+ 个人网页：https://bitbitcode.github.io/
+ 开源地址：https://gitee.com/Acrylic-Studio/Mathematical-Statistics

更新日志
-------
+ 创建日期：2020.9.20

Copyright (c) Acrylic Studio. All rights reserved.
"""


# 【导入库】
# 第三方库
import math
# 自定义库
from dapas.basefunction import *
from dapas.statistics import *


# 【概率密度函数】
# 均匀分布
def unif(x, min=0, max=1):
    """
    【函数说明】

    功能：均匀分布的概率密度函数（Uniformity）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + min：[float 浮点型] 区间左端点的横坐标值，若省略则默认为0
    + max：[float 浮点型] 区间右端点的横坐标值，若省略则默认为1

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    if (min < x < max):
        y = 1 / (max - min)
        return y
    else:
        return 0


# 指数分布
def exp(x, k=1):
    """
    【函数说明】

    功能：指数分布的概率密度函数（Exponent）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + k：[float 浮点型] 指数分布的参数，若省略则默认为1

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    if (x > 0):
        y = k * math.exp(-k*x)
        return y
    else:
        return 0


# 二项分布
def binom(x, p, n=1):
    """
    【函数说明】

    功能：二项分布的概率密度函数（Binomial Distribution），默认为(0,1)分布

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + p: [float 浮点型] 概率
    + n：[int 整形] 试验次数，若省略则默认为1

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    y = C(n, x) * (p**x) * ((1-p)**(n-x))
    return y


# 泊松分布
def pois(x, Lambda):
    """
    【函数说明】

    功能：泊松分布的概率密度函数（Poison Distribution）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + Lambda：[float 浮点型] 泊松分布的参数（λ）

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    k = 0   # 这里有问题
    y = ((Lambda**k) * math.exp(-Lambda))/(fac(k))
    return y


# 几何分布
def geom(x, p):
    """
    【函数说明】

    功能：几何分布的概率密度函数（Geometry Distribution）

    参数：
    + x：[int 整型] 在第x次尝试取得第1次成功
    + p：[float 浮点型] 成功的概率

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    y = (1-p)**(x-1) * p
    return y


# 超几何分布
def hyper(x, n, M, N):
    """
    【函数说明】

    功能：超几何分布的概率密度函数（？ Geometry Distribution），超几何分布实际上是不放回抽样
    若N件产品中有M件次品，抽检n件时所得次品数X=k

    参数：
    + x：[int 整型] 
    + n：[int 整型]
    + M：[int 整型] 次品数
    + N：[int 整型] 样品总数 

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    y = C(M, x)*C(N-M, n-x) / C(N, n)
    return y


# 正态分布
def norm(x, Mu=0, Sigma=1):
    """
    【函数说明】

    功能：一般正态分布的概率密度函数（Normal），若省略期望与方差的参数，则为标准正态

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + Mu：[float 浮点型] 总体的期望（μ），若省略则0
    + Sigma：[float 浮点型] 总体的方差（σ） ，若省略则1

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    y = (1/((math.sqrt(2*math.pi))*Sigma)) * \
        math.exp(-((x-Mu)**2)/(2*Sigma**2))
    return y


# 标准正态分布
# def norm_s(x):
#     """
#     【函数说明】

#     功能：标准正态分布的概率密度函数（Standard Normal），样本期望为0，样本方差为1

#     参数：
#     + x：[float 浮点型] 某个样本点（x）的横坐标值

#     返回值：
#     + [float 浮点型] 该样本点（x）处的概率密度
#     """
#     y = (1/math.sqrt(2*math.pi)) * math.exp(-(x**2)/2)
#     return y


# Γ分布
def gamma(x, Alpha, Beta):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（Gamma Distribution）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + Alpha：[float 浮点型] （α>0）
    + Beta：[float 浮点型] （β>0）

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    if(x > 0):
        y = ((Beta**Alpha)/math.gamma(Alpha)) * \
            x**(Alpha-1) * math.exp(-Beta*x)
        return y
    elif(x <= 0):
        return 0


# Χ^2分布
def chisq(x, n):
    """
    【函数说明】

    功能：卡方分布的概率密度函数（Χ^2 Distribution）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    if(x > 0):
        y = gamma(x, (n/2), (1/2))
        return y
    elif(x <= 0):
        return 0


# β分布
def beta(x, a, b):
    """
    【函数说明】

    功能：β分布的概率密度函数（t Distribution）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + a：[float 浮点型] 
    + b：[float 浮点型] 

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    if(0 < x < 1):
        y = (math.gamma(a+b))/(math.gamma(a)*math.gamma(b)) * \
            (x**(a-1)) * ((1-x)**(b-1))
        return y
    elif(x <= 0):
        return 0


# t分布
def tdis(x, n):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（t Distribution）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值
    + n：[float 浮点型] 

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    y = math.gamma((n+1)/2)/(math.sqrt(math.pi*n) *
                             math.gamma(n/2)) * (1+(x**2/n))**(-(n+1)/2)
    return y


# 柯西分布
def cauchy(x):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（Cauchy Distribution）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    y = 1/(math.pi*(1+x**2))
    return y


# F分布
def fdis(x, n1, n2):
    """
    【函数说明】

    功能：标准正态分布的概率密度函数（F Distribution）

    参数：
    + x：[float 浮点型] 某个样本点（x）的横坐标值

    返回值：
    + [float 浮点型] 该样本点（x）处的概率密度
    """
    if(x > 0):
        y = (math.gamma((n1+n2)/2)*(n1/n2))/(math.gamma(n1/2)*math.gamma(n2/2)
                                             ) * ((n1/n2)*x)**((n1/2)-1) * (1+(n1*x/n2))**(-(n1+n2)/2)
        return y
    elif(x <= 0):
        return 0


# 【模块内测试代码】
if __name__ == "__main__":
    X_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in X_series:
        print("X~U(0,1)", x, "：", unif(x, 1, 5))
    for x in X_series:
        print("X~E(0,1)", x, "：", exp(x, 2))
    for x in X_series:
        print("二项分布：", binom(x, 0.3, 100))
else:
    print("【dapas.distribution加载成功】")
