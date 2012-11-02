# -*- encoding:utf-8 -*-
from prime import isprime, primes, isprime_2

def formula(n, a, b):
    if a >= 1000 or b >= 1000:
        return False
    else:
        return n ** 2 + a * n + b

def main():
    max_length = 0
    N = 1000
    _a, _b = 0, 0
    N_a = [i for i in xrange(-N, N) if i != 0]
    N_b = [i for i in xrange(-N, N) if i != 0]
    for i in N_a:
        a = i
        for j in N_b:
            b = j
            n = 0
            while True:
                ans = formula(n, a, b)
                if isprime_2(ans):
                    n += 1
                else:
                    break
            if n > max_length:
                _a, _b = a, b
                max_length = n

    print 'max_length =',max_length
    print 'formula = n ** 2 + n *',_a,'+',_b
    print '_a * _b =', _a * _b

if __name__ == '__main__':
    main()

    
