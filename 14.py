# -*- encoding:utf-8 -*-

def generate_num(n, num_list=None):
    if not num_list:
        num_list = [n]
    if n == 1:
        return len(num_list)
    if n % 2 == 0:
        num_list.append(n/2)
        return generate_num(num_list[-1], num_list)
    else:
        num_list.append(3 * n + 1)
        return generate_num(num_list[-1], num_list)

if __name__ == '__main__':
    value = 1000000
    ans = 0
    number = 0
    for i in xrange(1, value):
        num_list = None
        if i % 2 == 0:
            pass
        else:
            product = generate_num(i, num_list)
        if ans < product:
            number, ans = i, product
        print number, ans
    print number, ans


