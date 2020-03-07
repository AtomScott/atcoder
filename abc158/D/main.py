#!/usr/bin/env python3
from collections import deque

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    # Failed to predict input format
    S = deque(input())
    Q = int(input())
    direction = 1

    for _ in range(Q):
        query = input().split()
        t = int(query[0])

        if t == 1:
            direction = direction *  -1

        elif t == 2:
            f = int(query[1])
            c = query[2]
            if f == 1:
                # add to front
                if direction == 1:
                   S.appendleft(c)
                # add to back
                if direction == -1:
                   S.append(c)
            elif f == 2:
                # add to back
                if direction == 1:
                   S.append(c)
                # add to front
                if direction == -1:
                   S.appendleft(c)
    S = list(S)
    if direction == -1:
        S = S[::-1]

    print(''.join(S))
    pass

if __name__ == '__main__':
    main()