import sys
from math import factorial

def ncr(n, r, p): 
    # initialize numerator 
    # and denominator 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  
            p - 2, p)) % p 

def check(x, y):
    if x < y:
        tmp = x
        x = y
        y = tmp

    n = x - y
    x -= 2 * n

    if (x + y) % 3 == 0:
        return True
    else:
        return False
    

# Read
line = sys.stdin.readlines()[0]
X, Y = map(int,line.split(' '))

# if not check(X, Y):
#     print(0)
#     exit(0)

m = int(1/3 * (2*Y - X))
n = int(Y - 2 * m)

if n < 0 or m < 0:
    print(0)
else:
    p = m if m < n else n
    print(ncr(n+m, p))
