# -*- encoding:utf-8 -*-

def fib(n, p1=None, p2=None):
    if not p1 or not p2:
        if n <= 2:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    else:
        return p1 + p2

def get_order(num):
    ch = str(num)
    return len(ch)

def main():
    N = 1000
    n = 2
    fibs = [1, 1]
    while True:
        x = fib(n, fibs[n - 1], fibs[n -2])
        fibs.append(x)
        result = get_order(x)
        if result >= N:
            break
        else:
            n += 1
    print n + 1

if __name__ == '__main__':
    main()
