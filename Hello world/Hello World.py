# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:36:50 2018

@author: joshu
"""
#Lectue notes for testing on Kattis

import sys

def answer():
    return "Hello World!"

def solve():
    print(answer())
    
def test():
    assert answer() == "Hello World!"
    print('all test cases passed...')
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
    