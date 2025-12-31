from mpmath import mp

def compute_pi(digits):
    """ 使用Chudnovsky算法计算π到指定的位数 """
    # 设置mpmath的精度（位数）
    mp.dps = digits  # 设置小数点后的位数，包括整数部分，所以实际位数会稍微多一点
    pi = mp.pi
    return str(pi)

if __name__ == "__main__":
    digits = int(input("Enter the number of digits to calculate pi to: "))
    pi_value = compute_pi(digits)
    print("Pi computed to {} digits:".format(digits))
    print(pi_value)