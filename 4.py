# -*- encoding:utf-8 -*-

def iscircle(n):
    c = str(n)
    for i in xrange(int(len(c)/2)):
        if not c[i] == c[-(i+1)]:
            return False
    return True

def ismulti(n):
    for i in xrange(100, 1000):
        if n%i == 0:
            if n/i > 999:
                continue
            else:
                return True
    return False

if __name__ == '__main__':
    a = 100 * 100
    b = 999 * 999
    ans = []
    for i in xrange(a, b):
        if iscircle(i):
            if ismulti(i):
                print 'OK', i
                ans.append(i)
    print ans[-1]
                
    
