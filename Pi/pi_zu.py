# Zu Chongzhi 于 5世纪发明的公式
# π = √(10(1 + √5)) / 2(2 + √5)

from math import sqrt

def calculate_pi() -> float:
    return sqrt(10 * (1 + sqrt(5))) / (2 * (2 + sqrt(5)))

print(calculate_pi())
