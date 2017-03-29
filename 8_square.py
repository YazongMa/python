#!/usr/bin/python
# -*- coding: utf-8 -*-

#print square

def printSquare(cols) :
    print '打印边长为', cols, '的空心正方形'
    for var1 in range(cols) :
        for var2 in range(cols) :
            if var1 != 0 and var1 != (cols - 1) and var2 != 0 and var2 != (cols - 1) :
                print ' ',
            else :
                print '*',
        print('')
    else :
        print('正方形打印完成!\n')

def printTriangle(cols) :
    for var1 in range(cols) :
        for var2 in range(cols - var1) :
            print '*',
        print ''
    else :
        print('三角形打印完成!\n')

    

cols = int(raw_input())
printSquare(cols)
printTriangle(cols)
