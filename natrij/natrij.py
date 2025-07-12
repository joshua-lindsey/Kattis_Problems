# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 12:39:29 2018

@author: joshu
"""

import sys
from datetime import timedelta

def hms_to_s(x):
    X = x[0]*60*60 + x[1]*60 + x[2]
    return X

def countdown(C, B):
    c = hms_to_s(C)
    b = hms_to_s(B)        
    if b == c:
        t = '24:00:00'
    if b > c:
        sec = b - c
        t = str(timedelta(seconds = sec))
    if b < c:
        sec = 24*60**2 - c + b
        t = str(timedelta(seconds = sec))
    if len(t) == 7:
        t = '0' + t
    return t   

def solve(ct1,bt1):
        ctx = [int(i) for i in ct1.split(':')]
        btx = [int(i) for i in bt1.split(':')]
        
        TIME = countdown(ctx, btx)
        
        return TIME
    
    
def test():
    assert solve('12:00:00', '23:59:59') == '11:59:59'
    assert solve('14:25:36', '15:47:15') == '01:21:39'
    assert solve('00:00:00', '23:59:59') == '23:59:59'
    assert solve('14:00:00', '14:00:00') == '24:00:00'
    print('all test cases passed')

if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1] == 'test'):
        test()
    else:
        current_time = [int(i) for i in input().split(':')]
        bomb_time = [int(i) for i in input().split(':')]

        time = countdown(current_time, bomb_time)
        
        print(time)