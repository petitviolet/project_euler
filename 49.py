# -*- encoding:utf-8 -*-
from prime import *
from itertools import permutations as per

p = primes(10000)
prms = [n for n in p if 1000 < n < 10000]

def cycle(n):
    s = str(n)
    nums = [int(''.join(i)) for i in per(s) if int(''.join(i)) > n and isprime_2(int(''.join(i)))]
    for num in nums:
        sub = num - n
        for _num in nums:
            _sub = _num - num
            if _sub == sub:
                return int(str(n) + str(num) + str(_num)), sub
    return False, False

def main():
    global prms
    _ans = []
    _sub = []
    for prm in prms:
        ans, sub = cycle(prm)
        if ans:
            _ans.append(ans)
            _sub.append(sub)
        else:
            continue
    for i, a in enumerate(_ans):
        print a, '公差 =', _sub[i]

if __name__ == '__main__':
    main()
