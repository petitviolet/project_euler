# -*- encoding:utf-8 -*-

def main():
    n, interval, s, result = 1, 0, 1, 1
    nums = []
    while True:
        if n == s ** 2:
            interval += 2
            s += 2
        else:
            n += 1 * interval
            if n > 1001 * 1001:
                break
            result += n
            nums.append(n)

    print nums
    print result

if __name__ == '__main__':
    main()


    
