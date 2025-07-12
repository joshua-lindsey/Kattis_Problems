# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 09:53:06 2018

@author: joshu
"""

from collections import defaultdict

votes = defaultdict(lambda: 0)

while True:
    line = str(input())
    if line == '***':
        break
    elif line:
        votes[line] += votes[line]
    else:
        break

print(votes)
'''
peeps = ['a','a','a','b','c','d']    

num_votes = []

for i in range(len(votes)):
    count = 0
    for j in range(len(votes)): 
        if votes[i] == votes[j]:
            count += 1

    num_votes.append(count)

print(num_votes)

max_votes = max(num_votes)
print(max_votes)
'''