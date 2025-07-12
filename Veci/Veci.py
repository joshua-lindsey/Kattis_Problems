# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:18:34 2018

@author: joshu
"""

l1, l2, time = map(int, input().split())

for i in range(1, time+1):
    if (i % l1 == 0 and i % l2 == 0):
        print('yes')
        break
    else:
        if i == time:
            print('no')
        pass