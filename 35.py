# -*- encoding:utf-8 -*-
from math import sqrt

def isprime(n):
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cycle(n, head=None):
    if not isprime(int(n)):
        return False
    ch = str(n)
    length = len(ch)
    if not head:
        head = n
    ch_list = []
    for c in ch:
        ch_list.append(c)
    pop_num = ch_list.pop()
    ch_list.insert(0, pop_num)
    ch_list = ''.join(ch_list)
    if length == len(ch_list):
        pass
    else:
        ch_list.insert(0, 0)
    if head == int(ch_list):
        return True
    if isprime(int(ch_list)):
        return cycle(ch_list, head)
    else:
        return False
        
def main():
    count = 1
    N = 1000000
    for i in xrange(3, N):
        if cycle(str(i), i):
            count += 1
    print 'count =',count

if __name__ == '__main__':
    main()
