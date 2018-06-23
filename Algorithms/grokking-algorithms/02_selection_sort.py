#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 02_selection_sort.py
# Author        : huangkeke
# Time          : 2018/6/23 21:25
# Contact       : hkkhuang@163.com
# Description	: 选择排序


def find_smallest(arr):
    """
    找出数组中最小的元素值
    :param arr:  待查找数组
    :return:  返回最小元素值的索引下标
    """
    # 将数组的第一个元素默认为当前最小值
    smallest = arr[0]
    # 数组中最小值的下标
    smallest_index = 0

    # 遍历整个数组，查找中最小值
    for i in range(1, len(arr)):
        # 将数组中第2个到最后一个元素一次和当前最小值比较，找出最小值
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    # 返回最小值的下标
    return smallest_index


def selection_sort(arr):
    """
    选择排序
    :param arr: 待排序数组
    :return: 返回完成选择排序的新数组
    """
    # 定义一个新数组，依次将每一轮找到的当前轮最小的值添加进去
    new_arr = []
    # 对数组进行len(arr)轮选择，每轮选择出一个最小的数值
    for i in range(len(arr)):
        # 调用find_smallest函数找出当前轮最小的数值
        smallest = find_smallest(arr)
        # 每次找到一个最小的数值，将该数值从原数组中弹出，添加到新的数值中
        new_arr.append(arr.pop(smallest))

    # 整个数组完成选择排序，返回完成选择排序后的新数组
    return new_arr


def main():
    arr = [28, 24, 14, 9, 4, 23, 12]
    print(selection_sort(arr))


if __name__ == '__main__':
    main()

# output: [4, 9, 12, 14, 23, 24, 28]
