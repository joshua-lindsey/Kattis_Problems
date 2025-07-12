# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:08:50 2018

@author: joshu
"""

def moveDisks(n, src, helper, dst):
    if n > 0:
        moveDisks(n-1, src, dst, helper)
        print('Move disk #{} from {} to {}'.format(n, src, dst))
        moveDisks(n-1, helper, src, dst)
        
moveDisks(3, 'needle1', 'needle2', 'needle3')