# -*- encoding:utf-8 -*-


def gcd(a, b):
    while b > 0:
        a, b = b, a%b
    return a

def gad(a, b):
    return a*b / gcd(a, b)

if __name__ == '__main__':
    ans = reduce(gad, xrange(2, 21))
    print ans
    
