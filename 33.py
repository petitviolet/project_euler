# -*- encoding: utf-8 -*-


def fract(i, j):
    if i == j:
        return False
    p = str(i)
    q = str(j)
    if p[0] == p[1]:
        if q[0] == q[1]:
            return False
        return [int(p[0]), int(q.replace(p[0], ''))]
    for _p in p:
        if _p in q:
            q = q.replace(_p, '')
            p = p.replace(_p, '')
            # print [p, q], '------------'
            if not p or not q:
                return False
            return [int(p), int(q)]
    return False

def check(i, j):
    div = 1.0
    _p0 = i
    _p1 = j
    for n in xrange(2, j):
        while 1:
            if i % n == 0 and j % n == 0:
                div *= n
                i /= n
                j /= n
            else:
                break
    if div == 1 or div == 10:
        return False
    x = fract(_p0, _p1)
    if x:
        # print 'x =', x, 'div =', div, 'i, j =', [_p0, _p1]
        if x[0] * div == _p0 and x[1] * div == _p1:
            return j
    return False

def main():
    ans = 1.0
    bunsi = 49.0
    bunbo = 98.0
    for j in xrange(10, 100):
        for i in xrange(10, j):
            x = check(i, j)
            if x:
                # print i,j
                ans *= x
                bunsi *= i
                bunbo *= j
    print ans

if __name__ == '__main__':
    main()
