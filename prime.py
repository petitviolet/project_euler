# -*- encoding:utf-8 -*-
from math import sqrt
import math
from copy import deepcopy

def is_prime(n):
    '''
    素数の判定
    '''
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    r = math.floor(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f+2) == 0: return False
        f += 6
    return True

def isprime_2(n):
    '''
    素数の判定
    '''
    if n <= 1 or not n:
        return False
    if n == 2:
        return True
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def isprime(n, prms):
    '''
    単体では使えない
    '''
    for i in xrange(int(sqrt(n))):
        if n % prms[i] == 0:
            return False
    return True

def primes(n):
    '''
    ｎ以下の素数のリストを返す
    '''
    prms = [2]
    for i in xrange(3, n, 2):
        if isprime(i, prms):
            prms.append(i)
    return prms

if __name__ == '__main__':
    prms = primes(100)
    print '100以下の素数は'
    print prms
