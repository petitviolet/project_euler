# -*- encoding:utf-8 -*-
from prime import *
from copy import deepcopy as dp
prm = primes(1000000)
prms = [n for n in prm if n > 100000]


def change(n):
    s = str(n)
    length = len(s)
    for i in xrange(length - 1):
        for k in xrange(1, length - i):
            for j in xrange(1, 10):
                nums = []
                _s = dp(s)
                _n = int(s[:i] + str(i) + s[i+1:k] + str(i) + s[k+1:])
                if isprime_2(_n):
                    nums.append(_n)
            if len(nums) > 1:
                print len(nums)
            if len(nums) == 8:
                return min(nums)
        else:
            continue
    return False

def main():
    global prms
    for i in prms:
        print i
        ans = change(i)
        if ans:
            break
        else:
            continue
    print ans

if __name__ == '__main__':
    main()
