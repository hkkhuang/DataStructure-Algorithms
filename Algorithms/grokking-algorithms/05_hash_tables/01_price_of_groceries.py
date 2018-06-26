#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 01_price_of_groceries.py
# Author        : huangkeke
# Time          : 2018/6/26 10:36
# Contact       : hkkhuang@163.com
# Description	: 散列表-Python中以字典形式表示

# Python提供的散列表实现为字典，可使用函数dict来创建散列表。

# 创建空字典需要注意：
# 方式1：dict()
prices = dict()
# 方式2：{}
# prices = {}
prices['apple'] = 0.88
prices['milk'] = 1.23
prices['avocado'] = 2.15
print(prices)

print(prices['apple'])
# output: 0.88

price_books = {'apple': 0.88, 'milk': 1.23, 'avocado': 2.15}
print(price_books)
# output: {'apple': 0.88, 'milk': 1.23, 'avocado': 2.15}

print(price_books['apple'])
# output: 0.88
