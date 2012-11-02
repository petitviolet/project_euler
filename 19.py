# -*- encoding : utf-8 -*-

def get_day(y, m, d, past=0):
    if 28 <= d <= 29:
        if m == 2: 
            if y % 4 == 0 or y % 100 == 0:
                if y % 400 == 0:
                    uru = True
                uru = False
            else:
                uru = False
            if uru:
                if d == 28:
                    d += 1
                elif d == 29:
                    m, d = 3, 1
            else:
                if d == 28:
                    m, d = 3, 1
        else:
            d += 1
    elif d == 30:
        if m in [4, 6, 9, 11]:
            m, d = m + 1, 1
        else:
            d += 1
    elif d == 31:
        if m in [1, 3, 5, 7, 8, 10]:
            m, d = m + 1, 1
        elif m == 12:
            y, m, d = y + 1, 1, 1
    else:
        d += 1
    past += 1
    if y > 2000:
        return [False, False, False, False]
    return [y, m, d, past]

if __name__ == '__main__':
    y, m, d, past = 1901, 1, 1, 0
    ans = 0
    while True:
        [y, m, d, past] = get_day(y, m, d, past)
        print [y, m, d, past]
        if not y:
            break
        if d == 1:
            if y < 2001:
                if past % 7 == 0:
                    print past
                    ans += 1
    print ans
