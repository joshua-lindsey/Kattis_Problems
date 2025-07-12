# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:09:28 2018

@author: joshu
"""

import sys 

def answer(data):
    count = 0 
    for t in data:
        if t < 0:
            count +=1
    return count        

def answer1(line):
    return line.count('-')

def solve():
    #simple way to read one line 
    '''
    n_temp = int(input())
    temps = [int(n) for n in input().split()]
    '''
    #####  Read multiple lines 
    data = sys.stdin.readlines()
    n=int(data[0])
    temps = [int(i) for i in data[1].split()]
    print(answer1(data[1]))


def test():
    assert answer(1,2,3,4) == 1
    print('all tests casses passed...')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        solve()