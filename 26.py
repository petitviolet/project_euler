# -*- encoding:utf-8 -*-

def get_recur(n):
    num = str(1.0 / float(n))
    print num
    ch = num.split('.')[1]
    l = len(ch)
    for i in xrange(l):
        recur = ch[:i]
        j = 1
        while True:
            try:
                if recur == ch[(i * j) : (i * (j + 1))]:
                    j += 1
                else:
                    break
            except:
                if j >= 2:
                    print recur
                    return recur
                break
    return False

def cycle(n):
    while n % 2 == 0:
        n /= 2.0
    while n % 5 == 0:
        n /= 5.0
    if n == 1:
        return 0
    count = 1
    while 10**count % int(n) != 1:
        count += 1
    return count

def main():
    N = 1000
    recurs = {}
    for n in xrange(2, N):
        recur = cycle(n)
        recurs[n] = recur
    print recurs
    inverse = [(value, key) for key, value in recurs.items()] 
    print max(inverse)[1] 

if __name__ == '__main__':
    main()
