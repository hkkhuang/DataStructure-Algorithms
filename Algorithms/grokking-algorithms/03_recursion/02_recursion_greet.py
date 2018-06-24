#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 02_recursion_greet.py
# Author        : huangkeke
# Time          : 2018/6/24 20:58
# Contact       : hkkhuang@163.com
# Description	: 递归-调用栈
"""
栈一个特点：先进后出

一个重要概念：调用另一个函数时，当前函数暂停并处于未完成状态
"""


def greet(name):
    """
    演示调用栈
    :param name: 参数name
    :return:
    """
    print('hello, ' + name + '!')
    greet2(name)
    print('getting ready to say bye...')
    bye()


def greet2(name):
    print('how are you,' + name + '?')


def bye():
    print('ok,bye！')


def main():
    greet('hkkhuang')


if __name__ == '__main__':
    main()
