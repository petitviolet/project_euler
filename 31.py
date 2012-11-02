# -*- encoding:utf-8 -*-

def pond(limit=None):
    if not limit:
        limit = 200
    count = 0
    for a in xrange(3):
        money = a * 100
        _a_money = money
        for b in xrange(5):
            money += 50 * b
            _b_money = money
            for c in xrange(11):
                money += 20 * c
                _c_money = money
                for d in xrange(21):
                    money += 10 * d
                    _d_money = money
                    for e in xrange(41):
                        money += 5 * e
                        _e_money = money
                        for f in xrange(101):
                            money += 2 * f
                            g = limit - money
                            if 0 <= g <= 200:
                                count += 1
                                print 100*a, 50*b, 20*c, 10*d, 5*e, 2*f, 1*g
                            money = _e_money
                        money = _d_money
                    money = _c_money
                money = _b_money
            money = _a_money
    print count + 1 #200pond


if __name__ == "__main__":
    pond(200)


