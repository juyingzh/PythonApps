# 增长率计算
import matplotlib.pyplot as plt

rate = 0.1

## 增长率计算
# 上月非零：
#     （本月-上月）÷|上月|
# 上月为零：
#     若本月为零，则为0；
#     若本月非零，则=本月÷|本月|
def incrate(cur, pre):
    # cur: 本期值
    # pre: 上期值
    if pre!=0:
        res = (cur-pre)/abs(pre)
    else:
        if cur==0:
            res=0
        else:
            res=cur/abs(cur)
    return res

# 从负数到正数，计算增长率
data = list(range(-100, 100, 10))
inc=[]
for i in range(len(data)-1):
    inc.append(incrate(data[i+1], data[i]))

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.plot(data)
ax2.plot(inc)
# plt.show()

# 负数增长
i0=-100
data2=[i0]
for i in range(200):
    i1 = i0+abs(i0)*rate
    data2.append(i1)
    i0=i1

fig, ax = plt.subplots()
ax.plot(data2)
# plt.show()

# 正数增长
i0=0.01
data3=[i0]
for i in range(200):
    i1 = i0+abs(i0)*rate
    data3.append(i1)
    i0=i1

fig, ax = plt.subplots()
ax.plot(data3)
plt.show()