#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 05_quicksort.py
# Author        : huangkeke
# Time          : 2018/6/25 22:22
# Contact       : hkkhuang@163.com
# Description	: 快速排序


def quicksort(array):
    """
    快速排序
    :param array: 待排序列表
    :return: 完成排序的列表
    """
    # 基线条件,列表为空或者列表长度为1
    if len(array) < 2:
        return array

    # 递归条件
    else:
        # 选取基准值
        pivot = array[0]
        # 由所有小于基准值的元素组成的子列表
        less = [i for i in array[1:] if i > pivot]
        # 由所有大于基准值的元素组成的子列表
        greater = [i for i in array[1:] if i < pivot]

        # 返回由小于基准值子列表+基准值列表+大于基准值子列表
        return quicksort(less) + [pivot] + quicksort(greater)


def main():
    print(quicksort([3, 9, 6, 1, 7, 2, 8]))


if __name__ == '__main__':
    main()
