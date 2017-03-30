#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import calendar

#返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
ticks=time.time()
print 'time.time():            ', ticks

localtime=time.localtime(ticks)
print 'time.localtime():       ',localtime

asctime=time.asctime(localtime)
print 'time.asctime():         ',asctime

# 格式化成2016-03-20 11:45:39形式
strftime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
print strftime

# 格式化成Sat Mar 28 22:24:24 2016形式
strftime=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
print strftime
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
strftime=time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
print strftime

#time.altzone:返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
print 'time.altzone:                           ',time.altzone


#time.asctime([tupletime]):接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
print 'time.asctime():                         ',time.asctime()


#time.clock( ):用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
print 'time.clock():                           ',time.clock()


#time.ctime([secs]):作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print 'time.ctime():                           ',time.ctime()


#time.gmtime([secs]):接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
print 'time.gmtime():                          ',time.gmtime()


#time.localtime([secs]):接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
print 'time.localtime():                       ',time.localtime()


#time.mktime(tupletime):接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
print 'time.mktime():                          ',time.mktime(localtime)


#time.sleep(secs):推迟调用线程的运行，secs指秒数。
print 'time.sleep():                           ',time.sleep(1)


#time.strftime(fmt[,tupletime]):接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
print 'time.strftime():                        ',time.strptime(time.ctime())


#time.tzset():根据环境变量TZ重新初始化时间相关设置。 
#time.tzset()


print "\ncalendar.month(2017,3):"
print calendar.month(2017,3)

