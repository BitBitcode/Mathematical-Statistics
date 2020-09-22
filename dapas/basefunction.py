# 【库说明】
"""
数理统计系列库
============

简介
-------
+ 库名：dapas.basefunction.py
+ 功能：将一些经常用到的基础运算定义为函数

库函数
-------
+ fac(n)

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
import random
# 自定义库


# 【函数定义】
def fac(n):
    """
    【函数】

    功能：计算阶乘（Factorial）

    参数：
    + n：[int 整形]

    返回值：
    + [int 整形] 返回 n 的阶乘
    """
    if(not isinstance(n, int)):
        # 检查传入参数的数据类型是否正确（整形）
        raise TypeError("Param must be int!（参数需为整数！）")
    elif(n < 0):
        # 检查传入参数的值是否正确（非负数）
        raise ValueError("Param must be non-negative!（参数需为非负数！）")
    else:
        s = 1
        if (n == 0 or n == 1):
            return 1    # 0的阶乘为1，需要单独规定
        elif(n != 0 and n != 1):
            while(n != 0):
                s = s*n
                n = n-1
    return s


def A(n, m):
    """
    【函数】

    功能：计算排列数

    参数：
    + n：[int 整形]
    + m：[int 整形]

    返回值：
    + [int 整形]
    """
    # 调用的上层（阶乘函数）已进行了参数检查，此处无需重复检查
    y = fac(n)/fac(n-m)
    return int(y)


def C(n, m):
    """
    【函数】

    功能：计算阶乘（Factorial）

    参数：
    + n：[int 整形]
    + m：[int 整形]

    返回值：
    + [int 整形]
    """
    # 调用的上层（阶乘函数）已进行了参数检查，此处无需重复检查
    y = A(n, m)/A(m, m)
    return int(y)


def sample(N):
    """
    【函数】

    功能：生成 N 个随机数组成的样本

    参数：
    + N：[int 整形] 样本数量

    返回值：
    + [list 列表] 返回浮点型随机数的列表 
    """
    if(not isinstance(N, int)):
        # 检查传入参数的数据类型是否正确（整形）
        raise TypeError("Param must be int!（参数需为整数！）")
    elif(N <= 0):
        # 检查传入参数的值是否正确（非负数）
        raise ValueError("Param must be non-negative!（参数需为正数！）")
    else:
        S = []
        i = 0
        while(i < N):
            S.append(random.random())
            i = i+1
        return S


# 【模块内测试代码】
if __name__ == "__main__":

    N = [0, 1, 2, 3, 4, 5]
    for n in N:
        print("%d! =" % n, fac(n))

    n = 5.3
    m = 2

    # print("没有参数检验：A(", n, ",", m, ") = ", A_ns(n, m))
    # print("有参数检验：A(", n, ",", m, ") = ", A(n, m))
    # print("库函数：comb(", n, ",", m, ") = ", math.comb(n, m))

    # print("A(%d,%d) =", A(n,m))
    # print("C(", n, ",", m, ") = ", C(n, m))

    # print(type(N))
    # print(type(2.31))

    # print("2.5^3.14", -2.5**3.14)
    # print("2.5^3.14", pow(-2,3))
    # print("2.5^3.14", math.pow(-2.5,3.14))

    n = 10
    X = []
    X = sample(10)
    print(X)
    print(X[1])
