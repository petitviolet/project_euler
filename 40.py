# -*- encoding:utf-8 -*-

def make_run(N=1000000):
    product = '0'
    length = 0
    num = 1
    while length < N:
        product += str(num)
        num += 1
        length += 1
    ans = 1
    for i in xrange(6):
        ans *= int(product[10 ** i])
    return ans

def main():
    ans = make_run(1000000)
    print ans

if __name__ == '__main__':
    main()

