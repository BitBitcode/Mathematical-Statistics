#【库说明】



# 包含
import math


# 统计量函数
def sum(X):
    """
    【函数】求和
    """
    X_sum = 0
    for x_i in X:
        X_sum = X_sum + x_i
    return X_sum


def ave(X):
    """
    【函数】求平均值
    """
    n = len(X)
    X_ave = sum(X) / n
    return X_ave


def vari(X):
    """
    【函数】求方差（非修正）variance
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
    【函数】求修正方差 revise
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
    【函数】求标准差 Standard deviation
    """
    n = len(X)
    S = 0
    X_ave = ave(X)
    for x_i in X:
        S = S + (x_i - X_ave)**2
    X_std = math.sqrt(S / n)
    return X_std



# 模块内测试代码
if __name__ == "__main__":
    Sample = [18, 19, 18, 17, 20, 21, 23, 19, 16]
    print("求和为：", sum(Sample))
    print("平均值为：", ave(Sample))
    print("方差为：", vari(Sample))
    print("修正方差为：", vari_r(Sample))
    print("标准差为：", std(Sample))
