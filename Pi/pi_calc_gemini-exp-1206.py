'''
本程序由Gemini-exp-1206模型生成。

算法说明：

这个程序使用了 Chudnovsky 算法 来计算 π。Chudnovsky 算法是一种快速收敛的算法，比其他一些算法（如 Machin-like 公式）更快地计算出 π 的值。

注意：

  计算的位数越多，所需的时间和内存也越多。
  对于非常大的位数，可能需要很长时间才能完成计算。
  Python 的 decimal 模块可以处理任意精度的数字，但受限于计算机的内存。
'''

import decimal

def calculate_pi(precision):
    """
    使用 Chudnovsky 算法计算 π 到指定的精度。

    Args:
      precision: 要计算的 π 的位数。

    Returns:
      一个 decimal.Decimal 对象，表示计算出的 π 值。
    """
    decimal.getcontext().prec = precision + 1  # 设置精度

    C = 426880 * decimal.Decimal(10005).sqrt()
    L = 13591409
    X = 1
    M = 1
    K = 6
    S = L

    for i in range(1, precision):
        M = (K**3 - 16 * K) * M // i**3 
        L += 545140134
        X *= -262537412640768000
        S += decimal.Decimal(M * L) / X
        K += 12

    pi = C / S
    return pi

# 获取用户输入的精度
precision = int(input("请输入要计算的 π 的位数："))

# 计算 π
pi = calculate_pi(precision)

# 打印结果
print(f"π 计算到 {precision} 位的结果为：\n{pi}")
