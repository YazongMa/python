#!/usr/bin/python
# -*- coding: UTF-8 -*-

#两个必备参数
def testPrint(name, age) :
    print 'name is', name, 'and age is', age


#一个必备参数, 一个缺省参数
def testPrint(name, age = 21) :
    print 'name is', name, 'and age is', age

#变长参数
def testPrint1(*arg) :
    for var in arg : 
        print var,
    print

#匿名函数
add = lambda arg1,arg2:arg1+arg2;
testPrint('Lol1', 10)
testPrint('Lol2')
testPrint(name='Lol3',age=23)
testPrint1(1,2,3,4,5,6)
print 'add(10,20):',add(10,20)
