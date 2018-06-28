#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 01_breadth-first_search.py
# Author        : huangkeke
# Time          : 2018/6/28 12:51
# Contact       : hkkhuang@163.com
# Description	: 广度优先搜索算法实现
from collections import deque

def create_graph():
    """
    创建图
    :return: 返回创建好的图
    """
    graph = {}
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom', 'jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['jonny'] = []
    return graph


def person_is_seller(name):
    """
    判断某个人是否为芒果销售商
    芒果销售商的条件是，姓名是以m结尾
    :param name:
    :return:
    """
    # 这里的判断条件 纯属为了演示
    return name[-1] == 'm'


def search_mango_seller(name, graph):
    """
    搜索芒果销售商
    :return: 搜索结果
    如果搜索到芒果销售商则输出信息"XX is a mango seller!",返回True
    没有搜索到则返回False
    """
    # 创建一个队列
    search_queue = deque()
    # 将你的邻居都加入到这个搜索队列中
    search_queue += graph[name]
    # 已经检查过的人
    searched = []

    # 未找到满足条件芒果销售商，只要队列不空，一直查找
    while search_queue:
        # 出队  取出其中的第一个人
        person = search_queue.popleft()
        if person is not in searched:
            # 仅当这个人没有被检查过的时候才检查
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
        else:
            # 不是芒果销售商，将这个人的朋友都加入到搜索序列
            search_queue += graph[person]
            # 将这个人标记为已经检查过
            searched.append(person)
    return False


def main():
    search_mango_seller('you', create_graph())


if __name__ == '__main__':
    main()
