# -*- encoding: utf-8 -*-
from copy import deepcopy

def main():
    tri = parse_triangle()
    #for x in tri:
    #    print x
    dic = []
    while len(tri) != 1:
        last,before_last = tri.pop(),tri[-1]
        _dic = []
        for i,x in enumerate(before_last):
            index = i
            if len(dic) != 0:
                _dic.append([x] + dic[index])
            else:
                _dic.append([x])
            #_dic[i] = [x] + dic[index] if len(dic)!=0 else [x]
            before_last[i] = x + max( last[i], last[i+1] )
        dic[:] = _dic
    for x in dic[0]:
        print x
    print tri[0][0]

def parse_triangle(input='tri_18.txt'):
    f = open(input)
    rows = filter(lambda x: x != '' , f.read().split('\n'))
    #tri = [map(int,r.split(' ')) for r in rows]
    tri = []
    for r in rows:
        tri.append((r.split(' ')))
    f.close()
    return tri

def tris(n):
    length = len(n)
    nn = [[] for l in xrange(length)]
    for i in xrange(length):
        if n[i] == '' or n[i] == ' ':
            nn[i] = 0
        else:
            nn[i] = int(n[i])
    sums = []
    sums.append(nn[0])
    for i in xrange(length - 1):
        p = max(nn[i], nn[i + 1])
        sums.append(p)
    return sums

def max_seq(sums):
    result = [[] for l in xrange(len(sums[0]))]
    prev = deepcopy(sums[0])
    next = deepcopy(sums[1])
    for i in xrange(len(sums) - 1):
        for l in xrange(len(prev) - 1):
            temp = next[l + 1] + max(prev[l], prev[l + 1])
            print temp,
            result[i].append(temp)
        prev, next = deepcopy(result[i]), deepcopy(sums[i + 1])
        print ''
    return result
if __name__ == '__main__':
    main()
    # input = 'tri_18.txt'
    # tri = parse_triangle(input)
    # length = len(tri)
    # sums = [[] for l in xrange(length)]
    # values = [[] for l in xrange(length)]
    # for i in xrange(length):
    #     #num -= 2
    #     t = tris(tri.pop())
    #     sums[i] = t
    #     print sums[i]
    # print sums
    # result = max_seq(sums)
    # print result
