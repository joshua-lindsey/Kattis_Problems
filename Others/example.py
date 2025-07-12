# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 09:32:12 2018

@author: joshu
"""

participants = input()
dice_throws = input().split(' ')

#get the amount of occurrences
pro = {i:dice_throws.count(i) for i in dice_throws}

nl = {}

for key, value in enumerate(dice_throws):
	#check if value is not in nl and it only occures 1 time
	if value not in nl and pro[value] == 1:
		nl[key + 1] = value
		# + 1 because we want a human readable index

if not nl:
	print ("none")
else:
	print (max(nl, key=lambda k: nl[k]))
	#get index with the highest value