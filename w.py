# -*- encoding:utf-8 -*-
tri = [(i * (i + 1)) / 2 for i in xrange(30)]

def is_tri(n):
    global tri
    if n in tri:
        return True
    else:
        return False

def change(word):
    p = 0
    for w in word:
        p += (ord(w) - 64)
    return p

def filer(f='words.txt'):
    r = open(f).read()
    words = r.split('","')
    return words

def main():
    global tri
    print tri
    count = 0
    words = filer()
    for word in words:
        n = change(word)
        if is_tri(n):
            count += 1
            # print word, '---', n
            print word,
    print count

if __name__ == '__main__':
    main()
