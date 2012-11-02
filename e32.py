# -*- encoding:utf-8 -*-

def check(a, b):
    ch = str(a) + str(b) + str(a*b)
    checker = [i for i in xrange(1, 10)]
    for c in ch:
        print checker
        print c
        if c in checker:
            checker.remove(c)
        else:
            return False
    if len(checker) == 0:
        return True
    print len(checker)
    return False

def main():
    result = []
    for i in xrange(1000):
        for j in xrange(1000):
            if check(i, j):
                if not n in result:
                    result.append(n)
                print i, j, n
    print sum(result)

if __name__ == '__main__':
    main()




