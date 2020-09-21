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


# 【概率密度函数】
# 均匀分布
def f_uniformity(a, b, x):
    """
    【函数说明】
    
    功能：均匀分布的概率密度函数

    参数：
    + a：[浮点数] 区间左端点的横坐标值
    + b：[浮点数] 区间右端点的横坐标值
    + x：[浮点数] 某个样本点（x）的横坐标值
    
    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    if (a < x < b):
        return 1 / (b - a)
    else:
        return 0


# 指数分布
def f_exponent(k, x):
    """
    【函数说明】
    
    功能：指数分布的概率密度函数

    参数：
    + k：[浮点数] 指数分布的参数
    + x：[浮点数] 某个样本点（x）的横坐标值
    
    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    if (x > 0):
        return k * math.exp(- k * x)
    else:
        return 0


# 正态分布
def f_norm(m, s, x):
    """
    【函数说明】
    
    功能：一般正态分布的概率密度函数

    参数：
    + m：总体的期望（μ）
    + s：总体的方差（σ）
    + x：[浮点数] 某个样本点（x）的横坐标值
    
    返回值：
    + [浮点数] 该样本点（x）处的概率密度
    """
    return (1/math.sqrt(2*math.pi)*s)*math.exp(-((x-m)**2)/(2*s**2))


# 标准正态分布
def f_norm_s(x):
    """
    【函数说明】
    
    功能：标准正态分布的概率密度函数

    参数：
    + 包含样本数据的Python列表
    
    返回值：
    + 列表中所有元素的标准差
    """
    return (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2)


# 


# 【模块内测试代码】
if __name__ == "__main__":
    X_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in X_series:
        print("X~U(0,1)", x, "：", f_uniformity(1, 5, x))
        print("X~E(0,1)", x, "：", f_exponent(5, x))
