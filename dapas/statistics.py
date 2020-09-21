#【库说明】
"""
【数理统计系列库】

简介
+ 库名：pystatistics.py
+ 功能：统计量函数

库函数
+ sum(X)
+ ave(X)
+ vari(X)
+ vari_r(X)
+ std(X)

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



# 【统计量函数定义】
def sum(X):
    """
    【函数】
    
    功能：计算样本的总和（Sum）

    参数：
    + [列表] 包含样本数据的Python列表
    
    返回值：
    + [浮点数] 列表中所有元素的总和
    """
    X_sum = 0
    for x_i in X:
        X_sum = X_sum + x_i
    return X_sum


def ave(X):
    """
    【函数】
    
    功能：计算样本的均值（Average）

    参数：
    + [列表] 包含样本数据的Python列表
    
    返回值：
    + [浮点数] 列表中所有元素的均值
    """
    n = len(X)
    X_ave = sum(X) / n
    return X_ave


def vari(X):
    """
    【函数】
    
    功能：计算样本的方差（Variance）

    参数：
    + [列表] 包含样本数据的Python列表
    
    返回值：
    + [浮点数] 列表中所有元素的方差
    """
    n = len(X)
    S = 0
    X_ave = ave(X)
    for x_i in X:
        S = S + (x_i - X_ave)**2
    X_vari = S / n
    return X_vari


def vari_r(X):
    """
    【函数】
    
    功能：计算样本的修正方差（Revise Variance）

    参数：
    + [列表] 包含样本数据的Python列表
    
    返回值：
    + [浮点数] 列表中所有元素的修正方差
    """
    n = len(X)
    S = 0
    X_ave = ave(X)
    for x_i in X:
        S = S + (x_i - X_ave)**2
    X_vari = S / (n+1)
    return X_vari


def std(X):
    """
    【函数】
    
    功能：计算样本的标准差（Standard deviation）

    参数：
    + [列表] 包含样本数据的Python列表
    
    返回值：
    + [浮点数] 列表中所有元素的标准差
    """
    n = len(X)
    S = 0
    X_ave = ave(X)
    for x_i in X:
        S = S + (x_i - X_ave)**2
    X_std = math.sqrt(S / n)
    return X_std



# 【模块内测试代码】
if __name__ == "__main__":
    Sample = [18, 19, 18, 17, 20, 21, 23, 19, 16]
    print("求和为：", sum(Sample))
    print("平均值为：", ave(Sample))
    print("方差为：", vari(Sample))
    print("修正方差为：", vari_r(Sample))
    print("标准差为：", std(Sample))
