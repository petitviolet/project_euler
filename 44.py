# -*- encoding:utf-8 -*-
from math import sqrt
tri = [n*(3*n - 1) / 2 for n in xrange(2, 10000)]

def check(n):
    global tri
    if n == 1:
        return False
    i = 2
    for i in xrange(0, n):
        _sum = tri[i] + tri[n]
        if isPentagonal(_sum):
            _sub = tri[n] - tri[i]
            if isPentagonal(_sub):
                print tri[n], ',', tri[i]
                return _sub
    else:
        return False

def isPentagonal(q):
    x = (1 + sqrt(1 + 24 * q)) / 6.0
    return int(x) == x

def main():
    n = 1
    while True:
        ans = check(n)
        if ans:
            break
        n += 1
    print 'ans =', ans

if __name__ == '__main__':
    main()

