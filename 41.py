# -*- encoding:utf-8 -*-
from prime import isprime_2 as isprime
from itertools import permutations as per

def check(n, order=None):
    if not order:
        order = len(str(n))
    c = [str(i) for i in xrange(1, order+1)]
    for _n in str(n):
        if _n in c:
            c.remove(_n)
        else:
            return False
    if len(c) == 0:
        return True
    else:
        return False

def pandigital(order):
    nums = [str(i) for i in xrange(1, order+1)]
    product = []
    for num in per(nums):
        num = ''.join(num)
        if isprime(int(num)) and check(num, order):
            product.append(int(num))
        else:
            continue
    if product:
        return max(product)
    else:
        return None

def main():
    orders = [i for i in xrange(1, 10)]
    orders.reverse()
    for order in orders:
        ans = pandigital(order)
        if ans:
            break
        else:
            continue
    print ans

if __name__ == '__main__':
    main()
            

