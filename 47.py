# -*- encoding:utf-8 -*-
from prime import *
from copy import deepcopy as dp
prms = primes(1000)

def solve(n):
    num = []
    for prm in prms:
        if prm > num:
            break
        while n % prm == 0:
            n /= prm
            num.append(prm)
    return set(num)

def main():
    n = 10
    _num = []
    length = 0
    while 1:
        num = solve(n)
        if len(num) == 4 and num != _num:
            _num = dp(num)
            length += 1
            print 'length =', length
            print n
        else:
            length = 0
        if length == 4:
            break
        n += 1
    print ''
    print n - 3
            
if __name__ == '__main__':
    main()



