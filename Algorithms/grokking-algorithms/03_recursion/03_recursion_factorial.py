#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 03_recursion_factorial.py
# Author        : huangkeke
# Time          : 2018/6/24 21:04
# Contact       : hkkhuang@163.com
# Description	: 递归-递归调用栈


def factorial(x):
    # 基线条件
    if x == 1:
        return 1
    # 递归条件
    else:
        return x * factorial(x - 1)


def main():
    print(factorial(5))


if __name__ == '__main__':
    main()


"""
小结：
递归指的是调用自己的函数。
每个递归函数都有两个条件：基线条件和递归条件。
栈有两种操作：压入和弹出。
所有函数调用都进入调用栈。
调用栈可能很长，这将占用大量的内存。
"""