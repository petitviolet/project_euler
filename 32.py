# -*- encoding:utf-8 -*-

def check(a, b, n):
    ch = str(a) + str(b) + str(n)
    if len(ch) != 9:
        return False
    checker = [str(i) for i in xrange(1, 10)]
    for c in ch:
        if c in checker:
            checker.remove(c)
        else:
            return False
    if len(checker) == 0:
        return True
    return False

def main():
    result = {}
    for i in xrange(2000):
        for j in xrange(i):
            n = i*j 
            if check(i, j, n):
                result[n] = 1
                print i, j, n
    print result.keys()
    print sum(result.keys())

if __name__ == '__main__':
    main()




