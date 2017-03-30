#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
python 列表
'''
list = ['run', 1, 3.14, 3+1j]

print 'list:                  ', list
print 'list[1:2]:             ', list[1:2]
print 'list[1:]:              ', list[1:]
print 'list*2:                ', list * 2

print 'list[2]:               ', list[2]
list[2] = 'test'
print 'modify list[2] to test:', list

tinylist = ['abc', 100]
print 'tinylist:              ', tinylist
print 'list[1:2] + tinylist:  ', list[1:2] + tinylist

print "\n"
#del list[2]:删除指定索引(2)项
del list[2]
print 'del list[2]:           ', list


#list.append(obj):在列表末尾添加新的对象
print 'list.append(0) return: ', list.append(0)
print 'after append(0):       ', list


#list.pop(obj=list[-1]):移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print 'list.pop(1) return:    ', list.pop(1)
print 'after pop(1):          ', list


#list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.extend(tinylist)
print 'list.extend(tinylist): ', list

#list.insert(index, obj):将对象插入列表
list.insert(1, 'python')
print 'list.insert(1, \'python\'):', list


#list.sort([func]):对原列表进行排序
list.sort()
print 'list.sort():           ',list

#cmp(list1, list2):比较两个列表的元素
list1 = [1,'2', 3.14]
list2 = [1,'2', 3.14, 3+14j]


print 'cmp(list1, list2):     ', cmp(list1, list2.pop())
