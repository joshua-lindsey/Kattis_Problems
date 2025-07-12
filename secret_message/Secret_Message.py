# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:11:30 2018

@author: joshu
"""

from math import ceil, sqrt

N = int(input())
for i in range(N):
  line = input()
  L = len(line)
  K = ceil(sqrt(L))
  M = K**2
  line += '*'*(M-L)
  
  tab = []
  for j in range(K):
    tab.append(list(line[K*j:K*(j+1)]))
    
  s = ''
  for y in range(K):
    for x in range(K):
      if tab[x][K-1-y] == '*':
        continue
      s = tab[x][K-1-y] + s
  print(s)