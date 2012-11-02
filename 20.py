# -*- encoding:utf-8 -*-

def fact(n):
    if n <= 2:
        return 2
    else:
        return n * fact(n-1)

if __name__ == '__main__':
    f = fact(100)
    st = str(f)
    ans = 0
    for s in st:
        ans += int(s)
    print ans

