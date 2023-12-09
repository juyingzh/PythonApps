'''
指数行情
'''
import urllib.request
import urllib.parse
url = "https://hq.sinajs.cn/list=hf_CHA50CFD"
rsp = urllib.request.urlopen(url)
print(rsp.read().decode('gbk'))
