# 计算圆周率的一种常见方法是使用数学公式：莱布尼兹级数
# π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)
# 参数 n_terms 指定了要计算的项数


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0
    for _ in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

print(calculate_pi(1000))
