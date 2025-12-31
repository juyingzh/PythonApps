# 速度较快，可以计算到10000位
# https://blog.csdn.net/wujuxKkoolerter/article/details/86152562
from decimal import Decimal
from decimal import getcontext
 
def cal_pi(precision):
    getcontext().prec=precision
    return sum(1/Decimal(16)**k * 
        (Decimal(4)/(8*k+1) - 
         Decimal(2)/(8*k+4) - 
         Decimal(1)/(8*k+5) -
         Decimal(1)/(8*k+6)) for k in range (precision))
 
print(cal_pi(1000))