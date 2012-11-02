# -*- encoding:utf-8 -*-
from math import sqrt
from prime import *
prms = primes(2000000)

def isprime(n):
    for i in xrange(2, 1+int(sqrt(n))):
        if n % i == 0:
            return False
    return True

def sumprimes(n):
    sum = 2
    for i in xrange(3, n):
        if isprime(i):
            sum += i
    return sum

def main():
    global prms
    ans = sum(prms)
    print ans
    # n = 2000000
    # ans = sumprimes(n)
    # print ans

if __name__ == '__main__':
    main()


