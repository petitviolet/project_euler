# -*- encoding:utf-8 -*-

def add_flow(n):
    i = str(n)
    sum = 0
    for j in i:
        sum += int(j)
    return sum

if __name__ == '__main__':
    ans = add_flow(2 ** 1000)
    print ans

