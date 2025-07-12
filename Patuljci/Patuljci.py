# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:04:00 2018

"""
import itertools

d1=int(input())
d2=int(input())
d3=int(input())
d4=int(input())
d5=int(input())
d6=int(input())
d7=int(input())
d8=int(input())
d9=int(input())

List=[d1,d2,d3,d4,d5,d6,d7,d8,d9]
stuff = []

for subset in itertools.combinations(List, 7):
    stuff.append(list(subset))

for n in range(len(stuff)):
    k=0
    for m in range(len(stuff[n])):
        k += stuff[n][m]
    if k == 100:
        C = stuff.index(stuff[n])
    else:
        pass

for i in range(len(stuff[C])):
    print(stuff[C][i])
     