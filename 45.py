# -*- encoding:utf-8 -*-
from math import sqrt

def isT(n):
    '''
    三角数かどうか
    '''
    x = (1 + sqrt(1 + 24 * n)) / 6.0
    return int(x) == x

def isP(n):
    '''
    五角数かどうか
    '''
    x = (1 + sqrt(1 + 8 * n)) / 2.0
    return int(x) == x

def create_H(i):
    return i * (2* i - 1)

def main():
    i = 144
    while 1:
        n = create_H(i)
        if isT(n) and isP(n):
            break
        i += 1
    print n

if __name__ == '__main__':
    main()

