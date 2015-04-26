__author__ = 'WangZhe'


def finddigit(a):
    n = 0
    while a >= 1:
        a //= 10
        n += 1
    return n

def KarastubaMultiplication(x, y):
    digitx = finddigit(x)
    digity = finddigit(y)

    a = x // 10**(digitx//2)
    b = y // 10**(digity//2)
    c = x - 10**(digitx//2)*a
    d = y - 10**(digity//2)*b

    if(digitx==0 or digity==0):
        return 0

    if(digitx==1 and digity==1):
        return x*y

    else:
        abterm = 10**(digitx//2+digity//2)*KarastubaMultiplication(a, b)
        adterm = 10**(digitx//2)*KarastubaMultiplication(a, d)
        bcterm = 10**(digity//2)*KarastubaMultiplication(b, c)
        cdterm = KarastubaMultiplication(c, d)
        return abterm+adterm+bcterm+cdterm

print(KarastubaMultiplication(131111233, 554))
