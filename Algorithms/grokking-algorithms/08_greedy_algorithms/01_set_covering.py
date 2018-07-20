#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Script Name   : 01_set_covering.py
# Author        : huangkeke
# Time          : 2018/7/19 8:29
# Contact       : hkkhuang@163.com
# Description	: 贪婪算法


def greedy():
    """
    贪婪算法-解决广播站覆盖问题
    :return:
    """
    # 需要覆盖的洲
    states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

    '''
    使用集合来表示要覆盖的州。集合类似于列表，只是同样的元素只能出现一次，即集合不能包含重复的元素。
    
    arr = [1, 2, 3, 4, 5, 1, 2, 3, 3, 1]
    print(set(arr))
    print(type(set(arr)))
    # {1, 2, 3, 4, 5}
    # <class 'set'>
    '''

    # 可供选择的广播台
    # 其中键为广播台的名称，值为广播台可以覆盖的洲
    stations = dict()
    stations['kone'] = set(['id', 'nv', 'ut'])
    stations['ktwo'] = set(['wa', 'id', 'mt'])
    stations['kthree'] = set(['or', 'nv', 'ca'])
    stations['kfour'] = set(['nv', 'ut'])
    stations['kfve'] = set(['ca', 'az'])

    # 存放最终选择的广播台
    final_stations = set()

    # 不断循环，直到states_needed为空
    while states_needed:
        # 遍历所有的广播台，选择覆盖了最多的未覆盖洲的广播台，存放在best_station中
        best_station = None

        # 存放一个广播台覆盖的所有未覆盖的洲
        state_covered = set()

        # 循环迭代每个广播台，确定是否为最佳的广播台
        for station, state in stations.items():
            # 计算交集
            # 并集意味着将集合合并。 交集意味着找出两个集合中都有的元素
            covered = states_needed & state

            if len(covered) > len(state_covered):
                # 将best_station设置为当前广播台
                best_station = station
                state_covered = covered

        # 将best_station添加到最终的广播台列表中
        final_stations.add(best_station)

        # 更新states_needed
        # 由于该广播台覆盖了一些州，因此不用再覆盖这些州
        states_needed -= state_covered

    return final_stations


def main():
    print(greedy())


if __name__ == '__main__':
    main()









