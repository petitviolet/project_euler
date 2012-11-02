# -*- encoding:utf-8 -*-

def sum_order(n):
    if n == 1:
        return False
    str_n = str(n)
    order = [int(s) for s in str_n]
    result = 0
    for o in order:
        if o == 0:
            pass
        else:
            result += o ** 5
    if n == result:
        return True
    else:
        return False

def main():
    ans = 0
    for i in xrange(1000000):
        if sum_order(i):
            print i
            ans += i
        i += 1
    print ans

if __name__ == '__main__':
    main()



