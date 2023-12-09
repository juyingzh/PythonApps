# 经典算法是使用欧拉公式
# π = √(6*∑(1/n^2))

from math import sqrt

def calculate_pi(n_terms: int) -> float:
    pi: float = 0.0
    for n in range(1, n_terms + 1):
        pi += 1 / (n ** 2)
    return sqrt(pi * 6)

print(calculate_pi(1000))
