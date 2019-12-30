import sys

def increment(asc, N):
    new_int = asc + N
    if new_int > ord('Z'):
        new_int = new_int - ord('Z') + ord('A') - 1
    return new_int

N = int(input())
S = input()

out = ''
for c in list(S):
    asc = ord(c)
    new_c = chr(increment(asc, N))
    out += new_c

print(out)