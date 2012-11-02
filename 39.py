# -*- encoding:utf-8 -*-
from math import sqrt as s

def check(i, j, k):
    max_len = max([i, j, k])
    if 2 * (max_len ** 2) == i ** 2 + j ** 2 + k ** 2:
        return True
    return False

def creat(i, num):
    _num = num / 2 - i
    for j in xrange(_num, num - i):
        if check(i, j, num-i-j):
            return True
    return False

def main():
    N = 1001
    _max = 0
    num = 0
    for i in xrange(12, N):
        print i,
        count = 0
        for j in xrange(1, i / 3):
            if creat(j, i):
                count += 1
        print '---', count
        if _max < count:
            _max = count
            num = i
    print 'max =', _max
    print 'num =', num

if __name__ == '__main__':
    main()



