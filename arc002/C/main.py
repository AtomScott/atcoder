#!/usr/bin/env python3

from itertools import product, permutations

def solve(C):
    commands = ['A','B','X','Y']
    combs = [''.join(comb) for comb in product(commands, commands)]

    mn_len = 10 ** 3 
    for L, R in product(combs, combs):
        new_c = C.replace(L, 'L').replace(R, 'R')
        mn_len = min(mn_len, len(new_c))
    print(mn_len)

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    C = input()
    solve(C)
    pass

if __name__ == '__main__':
    main()