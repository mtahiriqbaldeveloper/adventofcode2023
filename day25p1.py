#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 22:55:55 2023

@author: tiqbal
"""

import networkx as nx

g = nx.Graph()

for line in open("day25p1.txt"):
    left, right = line.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))