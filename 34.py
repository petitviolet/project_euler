# -*- encoding:utf-8 -*-

def analysis(n):
    if n <= 2:
        return False
    ch = str(n)
    result = 0
    for c in ch:
        result += fact(int(c))
    if result == n:
        return result
    else:
        return False

def fact(n):
    if n <= 1:
        return 1
    elif n <= 2:
        return 2
    else:
        return n * fact(n - 1)

def main():
    max_num = fact(9) * 4
    print 'max_num =', max_num
    ans = 0
    for i in xrange(3, max_num):
        a = analysis(i)
        if a:
            print a
            ans += a
    print ans

if __name__ == '__main__':
    main()
