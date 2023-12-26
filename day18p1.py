#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 08:36:34 2023

@author: tiqbal
"""

# =============================================================================
# points = [(0, 0)]
# dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
# 
# b = 0
# 
# for line in open("day18p1.txt"):
#     d, n, _ = line.split()
#     dr, dc = dirs[d]
#     n = int(n)
#     b += n
#     r, c = points[-1]
#     points.append((r + dr * n, c + dc * n))
# 
# A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
# i = A - b // 2 + 1
# 
# print(i + b)
# =============================================================================



points = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

b = 0

for line in open("day18p1.txt"):
    _, _, x = line.split()
    x = x[2:-1]
    dr, dc = dirs["RDLU"[int(x[-1])]]
    n = int(x[:-1], 16)
    b += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
i = A - b // 2 + 1

print(i + b)