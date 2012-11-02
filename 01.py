# -*- encoding:utf-8 -*-

def e1(num):
    sum = 0
    for i in xrange(num):
        if i%3==0 or i%5==0:
            sum += i
    return sum

if __name__=='__main__':
    sum = e1(1000)
    print sum
