#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 13:00:29 2023

@author: tiqbal
"""

# =============================================================================
# def extrapolate(array):
#     if all(x == 0 for x in array):
#         return 0
# 
#     deltas = [y - x for x, y in zip(array, array[1:])]
#     diff = extrapolate(deltas)
#     return array[-1] + diff
# 
# total = 0
# 
# for line in open("day9p1.txt"):
#     nums = list(map(int, line.split()))
#     total += extrapolate(nums)
# 
# print(total)
# =============================================================================
def extrapolate(array):
    if all(x == 0 for x in array):
        return 0

    deltas = [y - x for x, y in zip(array, array[1:])]
    diff = extrapolate(deltas)
    return array[0] - diff

total = 0

for line in open("day9p2.txt"):
    nums = list(map(int, line.split()))
    total += extrapolate(nums)

print(total)