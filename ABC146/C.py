import sys
import math
def d(N):
    return len(str(N))

def f(N, A, B):
    return A * N + B * d(N)

def resolve():
    line = input()
    A, B, X = map(int,line.split(' '))

    mn, mx = 0, 10**9+1

    while mx - mn > 1:
        N = (mn+mx)//2
        if X >= f(N, A, B):
            mn = N
        else:
            mx = N
            
    print(mn) 

if __name__ == '__main__':
    resolve()
