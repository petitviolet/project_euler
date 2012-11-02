# -*- encoding:utf-8 -*-
from math import sqrt

def pythagolas(n):
    for i in xrange(1, n):
        for j in xrange(1, n-i):
            k = sqrt(i * i + j * j)
            if k % 1 == 0.0:
                if i + j + k == n:
                    k = int(k)
                    print [i, j, k]
                    return i * j * k
    return None

if __name__ == '__main__':
    ans = pythagolas(1000)
    print ans
