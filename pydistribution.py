# 【库说明】


# 包含
import math
import pystatistics




# 【概率密度函数】
# 均匀分布
def f_uniformity(a, b, x):
    if (a < x < b):
        return 1/(b-a)
    else:
        return 0


# 指数分布
def f_exponent(k, x):
    if (x > 0):
        return k*math.exp(-k*x)
    else:
        return 0



# 正态分布
def f_norm(s,m,x):
    return (1/math.sqrt(2*math.pi))*math.exp(-((x-m)**2)/(2*s**2))


if __name__ == "__main__":
    X_series = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for x in X_series:
        print("X~U(0,1)", x, "：", f_uniformity(1, 5, x))
        print("X~E(0,1)", x, "：", f_exponent(5, x))
