from decimal import Decimal, getcontext
import math

def compute_pi(precision):
    """
    使用Chudnovsky算法计算π到指定的精度。
    :param precision: 想要计算的π的精度（小数点后的位数）
    """
    # 设置小数点精度
    getcontext().prec = precision + 1  # 加1以减少舍入误差

    # Chudnovsky算法的常数
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = L

    for i in range(1, precision):
        M = (K**3 - 16*K) * M // i**3 
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / X
        K += 12

    pi = C / S
    return pi

# 计算π到1000位
precision = 10000
pi = compute_pi(precision)
print(f"Pi to {precision} places:\n{pi}")