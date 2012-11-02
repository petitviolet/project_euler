# -*- encoding: utf-8 -*-
from math import sqrt

def isprime(n):
    for i in xrange(2, 1 + int(sqrt(n))):
        if n%i == 0:
            return False
    return True

def primes(i):
    prime, n = [], 2
    while len(prime) < i:
        if isprime(n) is True:
            prime.append(n)
        n += 1
    return prime

if __name__ == '__main__':
    ans = primes(10001)
    print ans[-1]
    
