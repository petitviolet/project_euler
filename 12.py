# -*- encoding:utf-8 -*-
from math import sqrt

def generate_tri(n):
    if n != 0:
        return n * (n + 1) / 2
    else:
        return 0

def get_divisor(n):
    div = 1
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            div += 2
    return div

def main():
    n = 1
    while True:
        tri = generate_tri(n)
        div = get_divisor(tri)
        if div <= 500:
            n += 1
        elif div > 500:
            break
    print tri

if __name__ == '__main__':
    main()
