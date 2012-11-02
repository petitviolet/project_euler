# -*= encoding:utf-8 -*-
from math import sqrt
from time import sleep

def isprime(n):
    if n == 2:
        return True
    elif n <= 1:
        return False
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def left_cut(n):
    ch = str(n)
    if ch[1] == 0:
        return None
    i = ch[1:]
    return int(i)

def right_cut(n):
    ch = str(n)
    if ch[-1] == 0:
        return None
    i = ch[:-1]
    return int(i)

def main():
    count = 0
    ans = 0
    num = 11
    while count < 11:
        left, right = num, num
        length = len(str(num))
        checker = True
        r, l = 1, 1
        if not isprime(num):
            num += 2
            continue
        while 1:
            try:
                if isprime(right):
                    right = right_cut(right)
                    if not right:
                        checker = False
                        break
                    r += 1
                else:
                    checker = False
                    r = length
                if isprime(left):
                    left = left_cut(left)
                    if not left:
                        checker = False
                        break
                    l += 1
                else:
                    checker = False
                    break
                if r == length or l == length:
                    break
            except:
                chcker = False
                break
        if checker:
            if isprime(right) and isprime(left):
                ans += num
                count += 1
                print num,'--',count
        num += 2
    print ans

if __name__ == '__main__':
    main()

                

