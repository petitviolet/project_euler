# -*- encoding:utf-8 -*-

def calc(a, b):
    return a ** b

def main():
    N = [i for i in xrange(2, 101)]
    result = {}
    for n_a in N:
        for n_b in N:
            result[calc(n_a, n_b)] = 1

    print len(result)

if __name__ =='__main__':
    main()

