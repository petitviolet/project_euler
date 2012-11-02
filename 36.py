# -*- encoding:utf-8 -*-

def binary(n):
    return format(n, 'b')

def iscycle(n):
    ch = str(n)
    for i in xrange(int(len(ch) / 2)):
        if ch[i] != ch[-(i + 1)]:
            return False
    return True

def main():
    ans = 0
    N = 1000000
    for i in xrange(N):
        if iscycle(i):
            if iscycle(binary(i)):
                ans += i
                print i
    print ans

if __name__ == '__main__':
    main()

    
