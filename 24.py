# -*- encoding:utf-8 -*-
from itertools import permutations

def main():
    min_num = 123456789
    dict = [min_num]
    while len(dict) < 1000000:
        numbers = [str(i) for i in xrange(10)]
        min_num += 9
        ch = str(min_num)
        if len(ch) == 9:
            ch = '0' + ch
        checker = True
        for c in ch:
            if c in numbers:
                numbers.remove(c)
                continue
            else:
                checker = False
                break
        if checker:
            print ch
            dict.append(ch)
    print dict[-1]

if __name__ == '__main__':
    #main()
    nums = [str(i) for i in xrange(10)]
    len = 0
    result = []
    for ch in permutations(nums, 10):
        result.append(ch)
        len += 1
        print ''.join(ch)
        if len == 1000000:
            print ''.join(ch)
            break


        

