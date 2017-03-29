#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
sep = 'o'
str = ' hello	world!  '
test = 'python' 
print 'str                              ' + str           
print 'str[0]                           ' + str[0]        
print 'str[2:5]                         ' + str[2:5]      
print 'str[2:]                          ' + str[2:]       
print 'str[2:3]                         ' + str[2:3]       
print 'str*2                            ' + str * 2 + '\n'        


#str.capitalize() : 将str的首字母大写
print 'str.capitalize()                 ', str.capitalize()

#str.center(40) : 将str移至指定宽度(40)中间,填充空格 
print 'str.center():                    ', str.center(40)


#str.count(sep, 2) : 从str[2]开始找出seq的个数
print 'str.count(sep, 2)                ', str.count(sep, 2)


#str.decode(encoding='UTF-8', errors='strict'):以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'
print 'str.decode()                     ', str.decode()


#str.encode(encoding='UTF-8', errors='strict'):以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
print 'str.encode()                     ', str.encode()


#string.expandtabs(tabsize=8): 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
print 'str.expandtabs()                 ', str.expandtabs()


#string.find(str, beg=0, end=len(string)):检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
print 'str.find(\'or\'))                ', str.find('or')


#string.index(str, beg=0, end=len(string)):跟find()方法一样，只不过如果str不在 string中会报一个异常
print 'str.index(\'or\'))               ', str.index('or')


#string.ljust(width):返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print 'str.ljust(40)                    ', str.ljust(40), str


#string.lstrip(): 截掉 string 左边的空格
print 'str.lstrip()                     ', str.lstrip()


#string.rstrip(): 截掉 string 右边的空格
print 'str.rstrip()                     ', str.rstrip()


#string.strip(): 截掉 string 左右边的空格
print 'str.strip()                      ', str.strip()


#string.partition(str)：把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string
print 'str.partition(\'o\')             ', str.partition('o')


#string.rpartition(str):类似于 partition()函数,不过是从右边开始查找.
print 'str.rpartition(\'o\')            ', str.rpartition('o')


#string.startswith(obj, beg=0,end=len(string)) : 检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查
print 'str.startswith(\'o\')            ', str.startswith('o')


#string.swapcase():翻转 string 中的大小写
print 'str.swapcase()                  ', str.swapcase()



#string.replace(str1, str2,  num=string.count(str1)):把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次
print 'str.replace(\'world\', \'python\')', str.replace('world', 'python')


