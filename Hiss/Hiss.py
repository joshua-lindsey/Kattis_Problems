# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:07:23 2018

@author: joshu
"""

import sys

def answer(x):
    if 'ss' in x:
        n = 'hiss'
    else:
        n = 'no hiss'
    return n

def solve():
    x = input()
    print(answer(x))

def test():
    assert answer('amiss') == 'hiss'
    print('all tests have passed...')
    
def test1():
    pass
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()   
    else:
        solve()        
        
      
        