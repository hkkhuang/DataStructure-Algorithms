#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 01_binary_search.py
# Author        : huangkeke
# Time          : 2018/6/21 17:09
# Contact       : hkkhuang@163.com
# Description	: 01-二分查找算法


def binary_search(search_list, item):
    """
    二分查找
    :param search_list:  待查找列表
    :param item: 匹配数值
    :return: 若在列表中查找到指定元素则返回位置索引，若没有找到则返回None
    """
    # low表示将查找列表的低位索引  high表示将查找列表的高位索引
    low = 0
    high = len(search_list) - 1

    # 查找范围没有缩小到只包含一个元素
    while low <= high:

        # 检查中间元素值
        mid = (low + high) // 2
        guess = search_list[mid]

        # 查找到指定元素
        if guess == item:
            # 返回索引位置
            return mid

        # 没有匹配，中间位置上元素值大于指定元素值，指定元素可能在左半边
        if guess > item:
            # 将高位索引改为 mid-1
            high = mid - 1
        # 没有匹配，中间位置上元素值小于指定元素值，指定元素可能在右半边
        else:
            # 将低位索引改为 mid+1
            low = mid + 1

    # 查找整个列表没有找到指定元素，返回None
    return None


# 构造一个待查找的列表
my_list = list(range(1, 20, 2))
print(my_list)
# output: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 查找11是否在列表中，存在返回位置索引  注意：索引从0开始
print(binary_search(my_list, 5))
# output: 5

# 查找12是否在列表中，不存在返回None None表示空，没有找到指定的元素
print(binary_search(my_list, 12))
# output: None

# *****************************************************************************************************************
# 二分查找输入必须是一个有序的元素列表。如果要查找的元素包含在列表中，返回其位置；否则返回null。
# 一般而言，对于包含n个元素的列表，用二分查找最多需要log n步(log指的都是log2)，而简单查找最多需要n步
