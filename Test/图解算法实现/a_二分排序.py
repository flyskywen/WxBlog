#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     二分排序
   Description :
   Author :        WX_PC
   Date：          2018-2018/10/1-14:58
   Email:          flyskywen@outlook.com
-------------------------------------------------
   Change Activity:
                   2018-2018/10/1-14:58
-------------------------------------------------
"""
__author__ = 'WX_PC'


# 有序列表,二分排序
# 时间复杂度 O(log n)
def binary_search(bin_list, item):
    low = 0
    high = len(bin_list) - 1

    while low <= high:
        # round 达到类似整除的效果
        # round返回的是四舍五入的值
        # 要达到四舍五入 import math
        # 应该使用math.floor
        mid = round((low + high) / 2)
        print(mid)
        guess = bin_list[mid]
        if guess == item:
            # 找到了元素
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


my_list = [i for i in range(1000)]
print(binary_search(my_list, 3))

print(my_list[8])
