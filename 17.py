# -*- encoding:utf-8 -*-
def generate(n):
    result = 0
    n = int(n)
    if n == 1 or n == 2 or n == 6:
        result += 3
    elif n == 4 or n == 5 or n == 9:
        result += 4
    else:
        result += 5
    return result

def num2words(num, depth=0):
    if num == 0: return 'zero'

    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tys = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    thousands = ['thousand','million','billion','trillion']

    words = []
    
    #last two digits
    x = num%100
    if x == 0:
        pass
    elif x >= 1 and x <= 9:
        words.append(units[x])
    elif x >= 10 and x <= 19:
        words.append(teens[x%10])
    else:
        words.append(units[x%10])
        words.append(tys[x//10])

    #3rd digit
    y = (num//100)%10
    if y == 0:
        pass
    else:
        if x != 0:
            words.append('and')
        words.append('hundred')
        words.append(units[y])

    #4th digit and above
    next = num2words(num//1000,depth+1)
    if next == 'zero':
        pass
    else:
        words.append(thousands[depth])
        words.append(next)
    return ' '.join(reversed(words))

if __name__ == '__main__':
    sum = 0
    for i in xrange(1, 1001):
        words = num2words(i)
        #print words
        sum += len(filter(lambda x:x!=' ',list(words)))
    print sum
