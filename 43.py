# -*- encoding:utf-8 -*-
from itertools import permutations

def pandigital():
    num = [str(i) for i in xrange(10)]
    pro = []
    for n in permutations(num):
        n = ''.join(n)
        pro.append(int(n))
    return pro

def check(p):
    s = str(p)
    if len(s) < 10:
        return False
    d_2 = int(s[1:4])
    if d_2 % 2 != 0:
        return False
    d_3 = int(s[2:5])
    if d_3 % 3 != 0:
        return False
    d_5 = int(s[3:6])
    if d_5 % 5 != 0:
        return False
    d_7 = int(s[4:7])
    if d_7 % 7 != 0:
        return False
    d_11 = int(s[5:8])
    if d_11 % 11 != 0:
        return False
    d_13 = int(s[6:9])
    if d_13 % 13 != 0:
        return False
    d_17 = int(s[7:])
    if d_17 % 17 != 0:
        return False
    return p

def main():
    numbers = pandigital()
    ans = 0
    for num in numbers:
        p = check(num)
        if p:
            ans += p
    print ans

if __name__ == '__main__':
    main()



