# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:28:14 2018

@author: joshu
"""
import sys
from math import sin, pi

def check_angle(h, ang):
    if (ang >= 0 and ang <= 180):
        status = 'safe'
    else:
        status = distance(h,ang)
    return status
    
def distance(H,A_deg):
    A_rad = A_deg * (pi / 180)
    return int(abs(H / sin(A_rad)))

def test():
    assert check_angle(10, 0) == 'safe'
    assert check_angle(100, 91) == 'safe'
    assert check_angle(1000, 180) == 'safe'
    assert check_angle(64, -45) == 90
    assert check_angle(10, 270) == 10
    assert check_angle(10, 225) == 14
    print('all test cases passed')

if __name__ == '__main__':
    if (len(sys.argv) > 1 and sys.argv[1] == 'test'):
        test()
    else:
        h, ang = map(int, input().split())
        print(check_angle(h, ang))
        