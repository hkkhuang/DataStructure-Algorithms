#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 01_Dijkstra's_algorithm.py
# Author        : huangkeke
# Time          : 2018/7/5 14:09
# Contact       : hkkhuang@163.com
# Description	: Dijkstra's_algorithm 狄克斯特拉算法

# graph 表示图 表现形式为散列表 （包含的其中元素还是散列表）
graph = dict()
# graph = {}

# graph['start'] 也是一个散列表，用来记录start节点邻居及权重
graph['start'] = {}
# 起点到a,b的权重   距离
graph['start']['a'] = 6
graph['start']['b'] = 2

# 获取起点的所有邻居
print(graph['start'].keys())
# output: dict_keys(['a', 'b'])

# 有一条从起点到A的边，还有一条从起点到B的边。获悉这些边的权重：
print(graph['start']['a'])
# output: 6

print(graph['start']['b'])
# output: 2

# 添加其他节点及邻居
graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

# 终点没有任何邻居节点
graph['fin'] = {}

# 节点的开销：从起点出发前往该节点需要多长时间
# 对于还不知道的开销使用无穷大表示  infinity = float('inf')

# 创建开销表
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 创建存储父节点的散列表
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = 'None'

# 定义一个数组，用于记录处理过的节点，对于同一个节点，不用处理多次
processed = []


def find_lowest_cost_node(costs):
    """
    找出开销最低的节点
    :param costs: 开销表
    :return: 返回找到的开销最小的节点， 没有则返回None
    """
    lowest_cost = float('inf')
    lowest_cost_node = None

    # 遍历所有的节点
    for node in costs:
        # 获取每个节点的开销
        cost = costs[node]

        # 如果当前节点的开销更低且未处理过
        if cost < lowest_cost and node not in processed:
            # 将其视为开销最低的节点
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


# node节点是找到的未处理的开销最低的节点
node = find_lowest_cost_node(costs)

# 只要还有未处理的节点则继续处理，直到所有的节点都处理完毕
while node is not None:
    # 获取该节点（开销表中未处理的开销最低的节点）的开销及邻居
    cost = costs[node]
    # neighbors是一个散列表 其邻居节点及开销
    neighbors = graph[node]

    # 遍历其所有的邻居节点
    for n in neighbors.keys():
        # 计算从起点到该节点的开销  计算方法是cost + neighbors[n] (cost相当于起点到当前最低开销节点的距离，
        # neighbors[n]是当前最低开销节点的距离到这个邻居的距离)
        new_cost = cost + neighbors[n]
        # 对新旧开销进行比较 如果找到一条更短的路径则更新开销表 父节点表
        if costs[n] > new_cost:
            # 更新开销表
            costs[n] = new_cost
            # 更新父节点表
            parents[n] = node
    # 将处理后的节点添加到 processed列表中
    processed.append(node)
    node = find_lowest_cost_node(costs)

print("从起点到各个节点的开销：")
print(costs)
# output:
# 从起点到各个节点的开销：
# {'a': 5, 'b': 2, 'fin': 6}
