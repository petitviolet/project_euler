# -*- encoding:utf-8 -*-
from math import sqrt
from copy import deepcopy

def isprime(n, prms):
    for i in xrange(int(sqrt(n))):
        if n % prms[i] == 0:
            return False
    return True

def primes(n):
    prms = [2]
    for i in xrange(3, n, 2):
        if isprime(i, prms):
            prms.append(i)
    return prms

def sum_divisor(num, prms):
    """真の約数の総和
    """
    div = {}
    if num in prms:
        return False
    n = num
    for prm in prms:
        count = 0
        if prm > n:
            break
        if n % prm == 0: #num = prm_1^count_1 * ... * prm_x^count_x
            count += 1
            n = n / prm
            while True:
                if n % prm == 0:
                    n /= prm
                    count += 1
                else:
                    break
            div[prm] = count

    divisor = 1.0
    for k, v in div.items():
        divisor *= float((k ** (v + 1) - 1) / (k - 1))
    value = divisor - num  #その数自体をひく
    if value > num:
        return True
    else:
        return False
    
def over_nums(n=28124, prms=None):
    return [i for i in xrange(1, int(n/2) + 1) if sum_divisor(i, prms)]

def _main():
    max_num = 28123 + 1
    prms = primes(max_num / 2)
    print len(prms)
    print max(prms)
    from time import sleep
    sleep(2)
    nums = over_nums(max_num, prms)
    _nums = deepcopy(nums)
    max_sums = sum(xrange(max_num))
    product = []
    print nums
    for num in nums:
        print len(_nums)
        for _num in _nums:
            p = _num + num
            product.append(p)
        _nums.remove(num)
    product = list(set(product))
    #_ans = sum(product.keys())
    _ans = sum(product)
    ans = max_sums - _ans
    print ans,'=',max_sums,'-',_ans


if __name__ == '__main__':
    _main()
