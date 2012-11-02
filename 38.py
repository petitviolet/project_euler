# -*- encoding:utf-8 -*-
from time import sleep
from itertools import *

def nine(n):
    if 123456789 < int(n) < 987654321:
        return True
    else:
        return False

def product(n, j):
    q = [str(n * i) for i in xrange(1, j+1) if (n * i) % 10 != 0]
    return q

def check(n):
    checker = [str(i) for i in xrange(1, 10)]
    for y in str(n):
        if y in checker:
            checker.remove(y)
        else:
            return False
    if len(checker) == 0:
        return True
    else:
        return False

def get_nums(j):
    # _nums = [(''.join(i)) for i in permutations(p, 2) if nine(int(''.join(i))) and check(''.join(i))]
    nums = []
    for i in xrange(2, 5):
        p = product(j, i)
        for c in combinations(p, i):
            num = ''.join(c)
            if not nine(num) or not check(num):
                continue
            else:
                # print num
                nums.append(int(num))
    if nums:
        return max(nums)
    else:
        return None

def main():
    N = 9876 + 1
    nums = []
    a = 0
    for i in xrange(1, N):
        if i % 5 == 0:
            continue
        g = get_nums(i)
        if a > g:
            continue
        nums.append(g)
        a = g
        print a, '---',i
    number = max(nums)
    print ''
    print number

if __name__ == '__main__':
    main()
