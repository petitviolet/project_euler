# -*- encoding:utf-8 -*-
from prime import *
N = 1000000
p = primes(N)
prms = [i for i in p if i < N]


def counter(n):
    global prms, N
    for i in xrange(N):
        if prms[i] > n:
            return 0
        _sum = 0
        j, count = 0, 0
        while _sum <= n:
            _sum += prms[i + j]
            count += 1
            if _sum == n:
                return count
            j += 1
    return 0

def _main():
    global N, prms
    ans = 0
    count, i = 0, 0
    for i in xrange(N):
        if ans + prms[i] > N:
            break
        ans += prms[i]
        count += 1
    for k in xrange(N):
        if is_prime(ans):
            print ans, count, sum(prms[k:i])
            break
        ans -= prms[k]
        count -= 1
        print ans

def main():
    global _prms, prms, N
    _max = 1
    _num = 0
    for prm in _prms:
        count = counter(prm)
        if count > _max:
            _max = count
            # print '--------------', count
            _num = prm
        print prm
    print _max, _num

if __name__ == '__main__':
    _main()
