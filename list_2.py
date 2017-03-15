#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
pythob 列表
'''
list = ['run', 1, 3.14, 3+1j]

print list
print list[1:2]
print list[1:]
print list*2

print list[2]
list[2] = 'test'
print list

tinylist = ['abc', 100]
print list[1:2] + tinylist