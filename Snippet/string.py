

## 在一个字符串序列里查找指定的字符串，找到则打印出来
for name in stock_zh_index_spot_df['名称']:
    if name.find('国证')!=-1:
        print(name)