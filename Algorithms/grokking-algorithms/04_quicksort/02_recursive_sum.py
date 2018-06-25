#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 02_recursive_sum.py
# Author        : huangkeke
# Time          : 2018/6/25 21:32
# Contact       : hkkhuang@163.com
# Description	: 求一个数组中所有元素和，使用递归


def recursive_sum(list):
    """
    求一个数组中所有元素和，使用递归
    :param list: 待求和列表
    :return: 列表数值和
    """
    # 递归基线条件
    if list == []:
        return 0
    # 递归条件
    else:
        return list[0] + recursive_sum(list[1:])


def main():
    print(recursive_sum([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
