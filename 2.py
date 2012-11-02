# -*- encoding:utf-8 -*-

def fib(n):
    a, b = 1, 2
    sum = []
    for i in xrange(n):
        sum.append(a)
        a, b = b, a + b
        if sum[-1] >= 4000000:
            return sum
    return sum

def adds(seq):
    ans = 0
    for s in seq:
        if s%2 == 0:
            ans += s
    return ans



if __name__ == '__main__':
    seq = fib(100)
    ans = adds(seq)
    print ans
        
