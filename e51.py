# -*- encoding:utf-8 -*-
from itertools import count, permutations
from prime import isprime_2 as is_prime
N = 8


def resolve(n):
    '''
    数字を各桁ごとに分割してリストに格納
    '''
    a = [ ]
    while n:
        a.append(n % 10);
        n /= 10
    return a

def unresolve(a):
    '''
    一桁の数字が各要素のリストをつなげて一つの数字に変換する
    '''
    n = 0
    for i in reversed(a):
        n = n * 10 + i
    return n

def embed(a, b, d):
    c = [ ]
    it = 0
    for e in b:
        if e:
            c.append(a[it])
            it += 1
        else:
            c.append(d)
    return c

def is_probable(a, b, min_p):
    d = 0
    if b[-1] == 0:
        d = 1
    return unresolve(embed(a, b, d)) < min_p

def get_min(a, b, min_p):
    global N
    if not is_probable(a, b, min_p):
        return 0
    counter = 0
    m = 0
    d_min = 0
    if b[-1] == 0:
        d_min = 1
    for d in range(9, d_min - 1, -1):
        p = unresolve(embed(a, b, d))
        if is_prime(p):
            m = p
            counter += 1
    
    if counter == N:
        return m
    else:
        return 0

def min_prime(n):
    min_p = 10 ** n
    for m in range(n - 3, 0, -3):
        pat = [ 1 ] * m + [ 0 ] * (n - m)
        for q in range(10**(m-1), 10**m):
            a = resolve(q)
            for b in permutations(pat):
                if b[0] == 0:
                    continue
                new_min_p = get_min(a, b, min_p)
                if new_min_p:
                    min_p = new_min_p
    
    if min_p < 10 ** n:
        return min_p
    else:
        return 0

def main():
    global N
    for n in count(5):
        m = min_prime(n)
        if m:
            print m
            break

if __name__ == '__main__':
    main()
