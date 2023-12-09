'''
get_quantile(data, t, linear=True, method='mean')

返回目标数t在给定列表data上的分位值。

Parameters:

    data: 给定的数值列表，长度大于1，其中不含空值（None）

    t: 目标数

    linear=True：逻辑值，是否去掉重复值后排序

    method='mean': {'mean', 'lower', 'higher'} 计算方法，'mean'取平均值，'lower'取较低值，'higher'取较高值

Returns

    分位值, 实数, 在[0, 1]之间
'''

def get_quantile(data, t, linear=True, method='mean'):

    data = [i for i in data if i]  # 去掉空值，类似pandas的dropna()

    if method not in {'mean', 'lower', 'higher'}:
        raise ValueError

    if linear:
        sorted_data=sorted(set(data))
    else:
        sorted_data=sorted(data)

    if len(sorted_data)<2:
        raise ValueError

    equal= False
    low = 0
    high = len(sorted_data)-1
    for i in range(len(sorted_data)):
        if t > sorted_data[i]:
            low = i
            continue
        elif t == sorted_data[i]:
            if equal == False:
                equal = True
                low = i
                continue
            else:
                continue
        else:
            if equal == True:
                high = i-1
                break
            else:
                high = i
                break
    # print("low={}, high={}".format(low, high))

    if method=='mean':
        return 0.5*(low+high)/(len(sorted_data)-1)
    elif method=='lower':
        return low/(len(sorted_data)-1)
    elif method=='higher':
        return high/(len(sorted_data)-1)
    else:
        return -1

if __name__ == '__main__':
    data = [1,2,3,3,3,4,5,6,7,7]
    # data = [1, 2, 3]
    # data = [2, 2]
    # data = [1, 2]
    # data = [1]
    t = 7 # -3.5 # 3 # 0 # 8 # 0.5 # 3.5 # 2 # 3 # 7 # 4.5 # 6 # 3.5 # 3
    p = get_quantile(data, t)
    # p = get_quantile(data, t, linear=False)
    # p = get_quantile(data, t, 'invalid')
    print("Percentile of {} in {} is {}".format(t, data, p))
