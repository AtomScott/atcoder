import sys

lines = sys.stdin.readlines()

N = int(lines[0].rstrip())
S = lines[1].rstrip()

if N % 2 == 1:
    print('No')
else:
    zenhan = S[:N//2]
    kouhan = S[N//2:]

    if zenhan == kouhan:
        print('Yes')
    else:
        print('No')