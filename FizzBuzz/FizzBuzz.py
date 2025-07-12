# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 09:38:10 2018

@author: joshu
"""
import sys

def answer(X,Y,n):
    if n%X == 0 and n%Y == 0:
        return 'FizzBuzz'
    elif n%X == 0:
        return 'Fizz'
    elif n%Y == 0:
        return 'Buzz'
    else:
        return n

def solve():
    X,Y,N = [int(i) for i in input().split()]
    for i in range(1, N+1):
        print(answer(X,Y,i))

def test():
    assert answer(5, 11, 55) == 'Fizzbuzz'
    assert answer(2, 3, 9) == 'Buzz'
    assert answer(6, 10, 24) == 'Fizz'
    assert answer(5, 11, 98) == 98
    
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test()
    else:
        solve()    