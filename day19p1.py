#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:00:05 2023

@author: tiqbal
"""
# =============================================================================
# 
# block1, block2 = open("day19p1.txt").read().split("\n\n")
# 
# workflows = {}
# 
# for line in block1.splitlines():
#     name, rest = line[:-1].split("{")
#     rules = rest.split(",")
#     workflows[name] = ([], rules.pop())
#     for rule in rules:
#         comparison, target = rule.split(":")
#         key = comparison[0]
#         cmp = comparison[1]
#         n = int(comparison[2:])
#         workflows[name][0].append((key, cmp, n, target))
# 
# ops = {
#     ">": int.__gt__,
#     "<": int.__lt__
# }
# 
# def accept(item, name = "in"):
#     if name == "R":
#         return False
#     if name == "A":
#         return True
# 
#     rules, fallback = workflows[name]
#     
#     for key, cmp, n, target in rules:
#         if ops[cmp](item[key], n):
#             return accept(item, target)
#     
#     return accept(item, fallback)
# 
# total = 0
# 
# for line in block2.splitlines():
#     item = {}
#     for segment in line[1:-1].split(","):
#         ch, n = segment.split("=")
#         item[ch] = int(n)
#     if accept(item):
#         total += sum(item.values())
# 
# print(total)
# 
# =============================================================================


block1, _ = open("day19p1.txt").read().split("\n\n")

workflows = {}

for line in block1.splitlines():
    name, rest = line[:-1].split("{")
    rules = rest.split(",")
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(":")
        key = comparison[0]
        cmp = comparison[1]
        n = int(comparison[2:])
        workflows[name][0].append((key, cmp, n, target))

def count(ranges, name = "in"):
    if name == "R":
        return 0
    if name == "A":
        product = 1
        for lo, hi in ranges.values():
            product *= hi - lo + 1
        return product
    
    rules, fallback = workflows[name]

    total = 0

    for key, cmp, n, target in rules:
        lo, hi = ranges[key]
        if cmp == "<":
            T = (lo, n - 1)
            F = (n, hi)
        else:
            T = (n + 1, hi)
            F = (lo, n)
        if T[0] <= T[1]:
            copy = dict(ranges)
            copy[key] = T
            total += count(copy, target)
        if F[0] <= F[1]:
            ranges = dict(ranges)
            ranges[key] = F
        else:
            break
    else:
        total += count(ranges, fallback)
            
    return total

print(count({key: (1, 4000) for key in "xmas"}))