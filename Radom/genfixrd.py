'''
生成固定大小的随机内容文件
用法：  genfixrd.py size unit e.g. 100 m
支持从B到TB大小

注：在生产大文件时这个程序性能不佳，慎用！
'''

#!/bin/env python
import os, sys

def createfile(filename, size):
    with open(filename,'wb') as f:
        f.write(os.urandom(size))
 
if len(sys.argv)<3:
    print("genfixrd.py size unit e.g. 100 m")
    sys.exit(1)

size = int(sys.argv[1])
unit = sys.argv[2][0].lower()
sm = {'b':1,'k':1024,'m':1024*1024,'g':1024*1024*1024,'t':1024*1024*1024*1024}

createfile("randata"+sys.argv[1]+unit, size*sm[unit])

print("gen randata"+sys.argv[1]+unit, "done") 
