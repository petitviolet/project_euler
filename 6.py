# -*- encoding : utf-8 -*-

def add(n):
    sum = 0
    for i in xrange(1, n+1):
        sum += i*i
    return sum

def multi(n):
    sum = 0
    for i in xrange(1, n+1):
        sum += i
    return sum ** 2

if __name__ == '__main__':
    a = add(100)
    b = multi(100)
    print b - a

