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
    for i in xrange(3, n+1, 2):
        if isprime(i, prms):
            prms.append(i)
    return prms

def sum_divisor(num, prms):
    """真の約数の総和
    """
    div = {}
    for prm in prms:
        if num % prm == 0: #num = prm_1^count_1 * ... * prm_x^count_x
            count = 1
            n = num / prm
            while True:
                if n % prm == 0:
                    n /= prm
                    count += 1
                else:
                    break
            div[prm] = count
    divisor = 1
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
    prms = primes((max_num) / 2)
    max_sums = sum(xrange(max_num))
    nums = over_nums(max_num, prms)
    _nums = deepcopy(nums)
    product = {}
    print nums
    for num in nums:
        print len(_nums)
        for _num in _nums:
            p = _num + num
            product[p] = 0
        del _nums[0]
    _ans = sum(product.keys())
    ans = max_sums - _ans
    print ans,'=',max_sums,'-',_ans



if __name__ == '__main__':
    prms = primes(28124)

    abundants = set(i for i in range(1,28124) if sum_divisor(i, prms))
    def abundantsum(i, abundants):
        return any(i-a in abundants for a in abundants)
    print sum(i for i in range(1,28124) if not abundantsum(i))
