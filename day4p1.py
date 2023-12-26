#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 14:22:01 2023

@author: tiqbal
"""
# =============================================================================
# 
# t = 0
# 
# for x in open("/Users/tiqbal/Documents/Leetcode/LeetCodeSol/src/main/java/adventofcode/day4/input.txt"):
#     x = x.split(":")[1].strip()
#     a, b = [list(map(int, k.split())) for k in x.split(" | ")]
#     j = sum(q in a for q in b)
#     if j > 0:
#         t += 2 ** (j - 1)
# 
# print(t)
# =============================================================================

m = {}

for i, x in enumerate(open("/Users/tiqbal/Documents/Leetcode/LeetCodeSol/src/main/java/adventofcode/day4/input.txt")):
    if i not in m:
        m[i] = 1

    x = x.split(":")[1].strip()
    a, b = [list(map(int, k.split())) for k in x.split(" | ")]
    j = sum(q in a for q in b)
    
    for n in range(i + 1, i + j + 1):
        m[n] = m.get(n, 1) + m[i]

print(sum(m.values()))