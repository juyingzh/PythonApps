import mpmath

def calculate_pi(digits):
    # 设置mpmath的精度，确保有足够的位数来存储结果
    mpmath.mp.dps = digits + 1  # 增加一位以确保精度
    pi_value = mpmath.mp.pi
    return str(pi_value)

if __name__ == "__main__":
    digits = int(input("请输入要计算的π的位数: "))
    pi_value = calculate_pi(digits)
    print(f"π的前{digits}位是: {pi_value}")
