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

#for循环
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print '当前水果 :', fruit

print 'range(3)', range(3)
rng_list = [0, 1, 2, 3]
for index in range(len(rng_list)) :
    print rng_list[index]

for index in range(len(fruits)):
    print fruits[index]
