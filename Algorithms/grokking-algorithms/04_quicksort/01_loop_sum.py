#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 01_loop_sum.py
# Author        : huangkeke
# Time          : 2018/6/25 21:29
# Contact       : hkkhuang@163.com
# Description	: 求一个列表中所有元素和，使用循环


def loop_sum(arr):
    """
    求一个列表中所有元素和，使用循环
    :param arr: 待求和数组
    :return: 数组之和
    """
    total = 0
    for x in arr:
        total = total + x
    return total


print(loop_sum([1, 2, 3, 4]))
# output: 10
