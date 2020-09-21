#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 【库说明】
"""
【数理统计系列库】

简介
+ 库名：pydistribution.py
+ 功能：概率密度函数与分布函数

库函数
+ f_uniformity(a, b, x)
+ f_exponent(k, x)

更多信息
+ 作者：Kiana Kaslana
+ 个人邮箱：smilewwc@qq.com
+ 个人网页：https://bitbitcode.github.io/
+ 开源地址：https://github.com/BitBitcode

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
    if (a < x < b):
        return 1 / (b - a)
    else:
        return 0


# 指数分布
def f_exponent(k, x):
    if (x > 0):
        return k * math.exp(- k * x)
    else:
        return 0


# 正态分布
def f_norm(m, s, x):
    return (1/math.sqrt(2*math.pi)*s)*math.exp(-((x-m)**2)/(2*s**2))


# 标准正态分布
def f_norm_s(x):
    return (1/math.sqrt(2*math.pi))*math.exp(-(x**2)/2)


# 


# 【模块内测试代码】
if __name__ == "__main__":
    X_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in X_series:
        print("X~U(0,1)", x, "：", f_uniformity(1, 5, x))
        print("X~E(0,1)", x, "：", f_exponent(5, x))
