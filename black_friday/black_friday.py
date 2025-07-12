# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 21:44:25 2018

@author: joshu
"""

group_size = int(input())
die_roll= list(map(int, input().strip().split()))

unique = []

for j in range(group_size):
    num = 0
    for i in range(group_size): 
        if die_roll[j] == die_roll[i]:
            num += die_roll.count(die_roll[i])

    if num == 1:
        unique.append(die_roll[j])
    else:
        pass
    
if not unique:
    print('none')
else:
    max_element = max(unique)
    element_loc = die_roll.index(max_element)
    print(element_loc + 1)
