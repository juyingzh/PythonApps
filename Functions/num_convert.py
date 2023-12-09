

def lower_zhnum(n):
    """
    将阿拉伯数字转换成小写汉字数字
    输入：
    n: int, 0-9
      给定阿拉伯数字
    输出：
    lower_zhnum: str, 
      小写汉字数字
    """
    if int(n) < 0 or int(n) >9:
        raise ValueError("数字超出范围")
    zhnums=['〇', '一', '二','三','四','五','六','七','八','九']
    return zhnums[int(n)]
# print(lower_zhnum(1.5))