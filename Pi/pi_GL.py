# 计算圆周率到任意精度的算法是使用 Gauss–Legendre 算法
# 它使用数学积分来计算圆周率。


from decimal import Decimal, getcontext

def calculate_pi() -> Decimal:
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)  # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s  # unary plus applies the new precision

print(calculate_pi())
