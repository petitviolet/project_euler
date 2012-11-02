# -*- encoding : utf-8 -*-
from math import sqrt

def d(n):
    sum = 1
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            sum += i
            if i == n/i:
                return sum
            else:
                sum += n/i
    return sum

if __name__ == '__main__':
    result = {}
    sum = 0
    for n in xrange(1, 10000):
        r = d(n)
        result[n] = r
    for k, v in result.items():
        try:
            if k == result[v]:
                if not k == v:
                    print k, result[k], 
                    print '==',v, result[v]
                    sum += k
        except KeyError:
            pass
    print sum
