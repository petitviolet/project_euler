# -*- encoding:utf-8 -*-

def filer(input):
    i = open(input, 'r').read()
    f = sorted(i.split(','))
    str_list = []
    for line in f:
        str_list.append(line.replace('"', ''))
    return str_list

def alpha(str_list):
    letv = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10, \
            'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19, \
            'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    ans = 0
    for i in xrange(len(str_list)):
        str_l = str_list[i]
        sum = 0
        for s in str_l:
            if s == '\n':
                continue
            x = letv[s]
            sum += x
        ans += sum * (i+1)
    return ans

if __name__ == '__main__':
    input = 'names.txt'
    str_list = filer(input)
    ans = alpha(str_list)
    print ans
