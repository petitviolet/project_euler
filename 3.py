# -*- encoding: utf-8 -*-
from math import sqrt

def isprime(n):
    for i in xrange(2, int(sqrt(n))):
        if n%i == 0:
            return False
    return True

def prime_factor(n):
    primes = []
    for i in xrange(2, int(sqrt(n))):
        if isprime(i):
            if n%i == 0:
                primes.append(i)
                n /= i
                if i > n:
                    return primes
    return primes

if __name__ == '__main__':
    ans = prime_factor(600851475143)
    print ans[-1]

