#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 03_recursive_count.py
# Author        : huangkeke
# Time          : 2018/6/25 22:06
# Contact       : hkkhuang@163.com
# Description	: 递归计数


def recursive_count(list):
    """
    递归函数计数
    :param list: 待计数列表
    :return: 列表中元素个数
    """
    # 基线条件
    if list == []:
        return 0
    # 递归条件
    else:
        return 1 + recursive_count(list[1:])


def main():
    print(recursive_count([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
