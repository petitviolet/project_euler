# -*- encoding:utf-8 -*-
from prime import *
N = 1000000
p = primes(500000)
prms = [i for i in p if i < N]


def counter(n):
    global prms, N
    for i in xrange(N):
        if prms[i] > n:
            return 0
        _sum = 0
        j, count = 0, 0
        print '---'
        while _sum <= n:
            _sum += prms[i + j]
            print prms[i+j]
            count += 1
            if _sum == n:
                return count
            j += 1
    return 0

def _main():
    global N, prms
    ans = 0
    count, i = 0, 0
    while ans < N:
        ans += prms[i]
        count += 1
        i += 1
    ans -= prms[i]
    count -= 1
    if isprime_2(ans):
        print ans
    else:
        while 1:
            print ans
            ans -= prms[i - 1]
            count -= 1
            i -= 1
            if isprime_2(ans):
                print ans, count
                break
            _ans = ans
            _count = count
            j = 0
            while j < 100:
                _ans -= prms[j]
                _count -= 1
                if isprime_2(ans):
                    print _ans, _count
                    break
                j += 1

def main():
    global prms, N
    _max = 1
    _num = 0
    for prm in prms:
        count = counter(prm)
        if count > _max:
            _max = count
            print '--------------', count
            _num = prm
        print prm
    print _max, _num

if __name__ == '__main__':
    _main()


