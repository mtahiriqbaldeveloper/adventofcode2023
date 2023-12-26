#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:59:36 2023

@author: tiqbal
"""

# =============================================================================
# def find_mirror(grid):
#     for r in range(1, len(grid)):
#         above = grid[:r][::-1]
#         below = grid[r:]
#         
#         above = above[:len(below)]
#         below = below[:len(above)]
#         
#         if above == below:
#             return r
#         
#     return 0
# 
# total = 0
# 
# for block in open("day13p1.txt").read().split("\n\n"):
#     grid = block.splitlines()
# 
#     row = find_mirror(grid)
#     total += row * 100
# 
#     col = find_mirror(list(zip(*grid)))
#     total += col
# 
# print(total)
# =============================================================================

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]
        
        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0

total = 0

for block in open("day13p1.txt").read().split("\n\n"):
    grid = block.splitlines()

    row = find_mirror(grid)
    total += row * 100

    col = find_mirror(list(zip(*grid)))
    total += col

print(total)