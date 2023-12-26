#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 07:38:09 2023

@author: tiqbal
"""

# =============================================================================
# times, distances = [list(map(int, line.split(":")[1].split())) for line in open("day6p1.txt")]
# 
# n = 1
# 
# for time, distance in zip(times, distances):
#     margin = 0
#     for hold in range(time):
#         if hold * (time - hold) > distance:
#             margin += 1
#     n *= margin
# 
# print(n)
# =============================================================================

times, distances = [list(map(int, ["".join(line.split(":")[1].split())])) for line in open("day6p2.txt")]

n = 1

for time, distance in zip(times, distances):
    margin = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            margin += 1
    n *= margin

print(n)