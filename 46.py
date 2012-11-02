# -*- encoding:utf-8 -*-
from prime import *
from math import sqrt
prms = primes(100000)
sq = [2 * (i * i) for i in xrange(1, 10000)]

def odds(n):
    n += 2
    while isprime_2(n):
        n += 2
    return n 

def main():
    global prms, sq
    n = 5
    flag = False
    while 1:
        for prm in prms:
            sub = n - prm
            if sub in sq:
                print n, '=', prm, '+', int(sqrt(sub/2)), '^ 2 * 2'
                break
        else:
            flag = True
            break
        if flag:
            print 'break'
            break
        n = odds(n)
    print 'n =', n

if __name__ == '__main__':
    main()
        
