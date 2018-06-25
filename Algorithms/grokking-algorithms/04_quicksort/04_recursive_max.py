#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 04_recursive_max.py
# Author        : huangkeke
# Time          : 2018/6/25 22:12
# Contact       : hkkhuang@163.com
# Description	: 使用递归找出列表中最大的数值


def max_value(list):
    """
    使用递归找出列表中最大的数值
    :param list:  待寻找最大值列表
    :return: 列表中最大元素值 注:列表为空时,返回None
    """
    # 基线条件
    if len(list) == 0:
        return None
    elif len(list) == 1:
        return list[0]

    # 递归条件
    else:
        temp_max_value = max_value(list[1:])
        #
        return list[0] if list[0] > temp_max_value else temp_max_value


def main():
    print(max_value([7, 5, 9, 23, 11]))


if __name__ == '__main__':
    main()
