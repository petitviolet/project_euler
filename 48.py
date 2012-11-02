# -*- encoding:utf-8 -*-

def num(n):
    return n ** n

def order_10(n):
    s = str(n)
    return s[-10:]

def main():
    n = 0
    for i in xrange(1, 1000):
        n += num(i)
    ans = order_10(n)
    print ans

if __name__ == '__main__':
    main()
