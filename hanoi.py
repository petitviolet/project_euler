def hanoi(n, from_, to, via):
    if n == 1:
        print "%s => %s" % (from_, to)
    else:
        hanoi(n - 1, from_, via, to)
        print "%s => %s" % (from_, to)
        hanoi(n - 1, via, to, from_)

if __name__ == '__main__':
    hanoi(6, 1, 2, 3)

