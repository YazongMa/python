#!/usr/bin/python
# -*- coding:utf-8 -*-

a = 21
b = 10
c = 0

if ( a != b ):
	print "a 等于 b"
	print "a:", a, "b:", b
else:
	print "a 不等于 b"
	print "a:", a, "b:", b

print "------------"

num = -1     
if num == 3:            # 判断num的值
    print 'boss'        
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出

if num != 3 and num != 2:            # 判断num的值
    print 'boss'        

