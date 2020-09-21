# 【库说明】
"""
【数理统计系列库】

简介
+ 库名：.py
+ 功能：将一些经常用到功能定义为函数

库函数
+ fac(n)

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


# 【函数定义】
def fac(n):
    """
    【函数】

    功能：计算阶乘（Factorial）

    参数：
    + n：[整数] 需要计算阶乘的数

    返回值：
    + [浮点数] n的阶乘
    """
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
    + n：[整数]
    + m：[整数]

    返回值：
    + [整数]
    """
    y = fac(n)/fac(n-m)
    return y


def C(n, m):
    """
    【函数】

    功能：计算阶乘（Factorial）

    参数：
    + n：[整数]
    +

    返回值：
    + [浮点数] n的阶乘
    """
    y = A(n, m)/A(m, m)
    return y


# 【模块内测试代码】
if __name__ == "__main__":
    N = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for n in N:
        print(fac(n))

    n = 5
    m = 2
    # C_nk = (fac(n))/((fac(k))*(fac(n-k)))
    # print(C_nk)

    print(A(n,m))
    print(C(n,m))
