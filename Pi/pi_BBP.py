# 使用 Bailey–Borwein–Plouffe (BBP) 公式计算圆周率
# BBP 公式允许在常数时间内计算圆周率的任意精度，而不像其他方法需要指数级的时间。

def calculate_pi(n_digits: int) -> str:
    pi: str = '3.'
    for i in range(1, n_digits + 1):
        pi += str(int(4 / (8 * i - 6) - 2 / (8 * i - 5) - 1 / (8 * i - 4)))
    return pi

print(calculate_pi(1000))
