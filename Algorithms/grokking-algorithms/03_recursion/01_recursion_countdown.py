#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 01_recursion_countdown.py
# Author        : huangkeke
# Time          : 2018/6/24 20:52
# Contact       : hkkhuang@163.com
# Description	: 递归-基线条件和递归条件
"""
每个递归函数都有两部分：基线条件（base case）和递归条件（recursive case）。
递归条件指的是函数调用自己，而基线条件则指的是函数不再调用自己，从而避免形成无限循环。
"""


def countdown(i):
    """
    递归演示
    :param i: 打印输出数字
    :return:  递归满足基线条件，结束，无返回值
    """
    print(i)
    # 基线条件
    if i <= 0:
        return
    # 递归条件
    else:
        countdown(i - 1)


def main():
    countdown(10)


if __name__ == '__main__':
    main()
