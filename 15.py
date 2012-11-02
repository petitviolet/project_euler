# -*- encoding: utf-8 -*-
from random import choice

def root(i, j):
    return pi(i + j) / (pi(i) * pi(j))

def pi(n):
    result = 1
    for i in xrange(1, n+1):
        result *= i
    return result

if __name__ == '__main__':
    ans = root(20, 20)
    print ans

    
