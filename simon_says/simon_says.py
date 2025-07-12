# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 10:25:46 2018

@author: joshu
"""

a = int(input())

line = 0
command  = []
command
while line < a:
    b = list(map(str, input().strip().split()))
    command.append(b)
    line += 1

simon=[]

for i in range(len(command)):
    if command[i][0] == 'simon' and command[i][1] == 'says':
        simon.append(command[i])

for i in range(len(simon)):
    simon[i][2:]
    
print(simon)        

for i in range(a):
    if k == 0:
        print(L)
    if k == len(simon) - 1:
        print(G)
        break
    else:
        print('\n')