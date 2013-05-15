# -*- encoding:utf-8 -*-

def e1(num):
    sum = 0
    for i in xrange(num):
        if 0 in (i%3, i%5):
            sum += i
    return sum

if __name__=='__main__':
    sum = e1(1000)
    print sum
