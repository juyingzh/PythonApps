'''
get_quantile_in(data, t, linear=True, method='mean')

返回目标数t在给定列表data上的分位值。与get_quantile功能相同，区别在于目标值t在data序列中

Parameters:

    data: 给定的数值列表，长度大于1，其中不含空值（None）。

    t: 目标数，是data序列中的值。

    linear=True：逻辑值，是否去掉重复值后排序

    method='mean': {'mean', 'lower', 'higher'} 计算方法，'mean'取平均值，'lower'取较低值，'higher'取较高值

Returns

    分位值, 实数, 在[0, 1]之间
'''

def get_quantile_in(data, t, linear=True, method='mean'):

    if t not in data:  # pandas的Series类型不能使用in判断
        raise ValueError("t not in data")

    data = [i for i in data if i]  # 去掉空值，类似pandas的dropna()

    if method not in {'mean', 'lower', 'higher'}:
        raise ValueError("method error")

    if linear:
        sorted_data=sorted(set(data))
    else:
        sorted_data=sorted(data)

    if len(sorted_data)<2:
        raise ValueError("data is too short")

    equal= False
    low = 0
    high = len(sorted_data)-1
    for i in range(len(sorted_data)):
        if t == sorted_data[i]:
            if equal == False:
                equal = True
                low = i
                high = i
                continue
            else:
                high = i
                continue
        else:
            if equal == True:
                 break
            else:
                continue
    print("low={}, high={}, length={}".format(low, high, len(sorted_data)))

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
    t = [-3.5, 2, 3, 3.5, 7, 4.5, 6, 8]
    p = get_quantile_in(data, t[4], linear=False, method='higher')
    # p = get_quantile(data, t, 'invalid')
    print("Percentile of {} in {} is {}".format(t[4], data, p))
