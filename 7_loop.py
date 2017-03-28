#!/usr/bin/python
#-*- coding:utf-8 -*-

#for循环
for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
    print '当前水果 :', fruit

#迭代 range
print 'range(3)', range(3)

for index in range(len(fruits)):
    print fruits[index]

print
#while循环
count = 0
while(count < 3) :
    print count
    count += 1

nums = [1,2,3,4,5,6,7,8,9,0]
new = []
old = []
print 'nums: ', nums
while len(nums) > 0 :
    num = nums.pop()
    if(num % 2 == 0) :
        new.append(num)
    else :
        old.append(num)
print 'new: ', new
print 'old: ', old


while 1 == 1 : 
    num = raw_input('Press q/Q exit! Enter a number: ')
    print 'you input: ', num
    if num == 'q' or num == 'Q' :
        break

