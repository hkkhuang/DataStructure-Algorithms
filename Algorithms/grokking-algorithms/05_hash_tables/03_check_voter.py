#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 03_check_voter.py
# Author        : huangkeke
# Time          : 2018/6/26 10:41
# Contact       : hkkhuang@163.com
# Description	: 散列表-防止重复

voted = {}


def check_voter(name):
    """
    检查投票人是否已经投过票
    :param name: 投票人姓名
    :return: 返回检查结果
    """
    # 检查散列表中（字典中）已经存在投票人信息，即已经投过票
    if voted.get(name):
        print('kick them out')
    # 没有投票
    else:
        # 记录投票信息
        voted[name] = True
        print('let them vote')


def main():
    check_voter('Tom')
    check_voter('Mark')
    check_voter('Jerry')
    check_voter('Tom')


if __name__ == '__main__':
    main()
