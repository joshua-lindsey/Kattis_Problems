# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:40:50 2018

@author: joshu
"""

width = int(input())
num_pieces = int(input())

piece = 0
area = 0

while piece < num_pieces:
    l,w = map(int, input().split())
    a = l*w
    area += a
    piece += 1

print(int(area /width))