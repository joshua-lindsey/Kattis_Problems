"""
Created on Tue Sep 25 17:28:29 2018

@author: joshu
"""

import sys



def quadrant(x,y):
    if (x>0 and y>0):
        quad = 1    
    elif (x<0 and y>0):
        quad = 2  
    elif (x<0 and y<0):
        quad = 3      
    else: 
        quad = 4
        print(quad)
        print(type(quad))
    return(type(quad))   

def testx(x):
    if type(x) == int or type(x) == float:
        return abs(x)
    else:
        return("Input is not an integer")
        
def test1(a,b):
    return(print(X))

def test2(x,y):
    assert quadrant(x,y) == 2
    print('Quadrant 2 passed...')

def test3(x,y):
    assert quadrant(x,y) == 3
    print('Quadrant 3 passed...')

def test4(x,y):
    assert quadrant(x,y) == 4
    print('Quadrant 4 passed...')
    
if __name__ == "__main__":
    X=int(input())
    Y=int(input())
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        testx(X,Y)
    elif len(sys.argv) > 1 and sys.argv[1] == 'test1':
        test1(X,Y) 
    elif len(sys.argv) > 1 and sys.argv[1] == 'test2':
        test2(X,Y)   
    elif len(sys.argv) > 1 and sys.argv[1] == 'test3':
        test3(X,Y) 
    elif len(sys.argv) > 1 and sys.argv[1] == 'test4':
        test4(X,Y)     
    else:
        quadrant(X,Y)   
        
print('imher',test1(1,1))        