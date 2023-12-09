# 使用 Nilakantha 级数，但它的计算机结果可比莱布尼茨公式更快地接近 Pi
# π = 3 + 4/(2*3*4) - 4/(4*5*6) + 4/(6*7*8) - 4/(8*9*10) + 4/(10*11*12) - (4/(12*13*14) ...
# 在该公式中，从 3 开始，依次交递加减以 4 为分子、三个连续整数乘积为分母的分数，每次迭代时三个连续整数中的最小整数是上次迭代时三个整数中的最大整数。
# 参数 n_terms 指定了要计算的项数


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 2.0
    operation: float = 1.0
    pi: float = 3.0
    for _ in range(n_terms):
        pi += operation * (numerator / (denominator*(denominator+1)*(denominator+2)))
        denominator += 2.0
        operation *= -1.0
    return pi

print(calculate_pi(1000))
