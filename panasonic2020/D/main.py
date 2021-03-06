#!/usr/bin/env python3
import sys
from itertools import combinations

def solve(N: int):   
    d = {n:[] for n in range(1, N+1)} 
    d[1] = [[1]]

    for n in range(1, N):
        
        for lst in d[n]:
            last_element = lst[-1]

            for new_element in range(1, max(lst)+2):
                d[n+1].append(lst+[new_element])

    ans_lst = d[N]

    for i, lst in enumerate(ans_lst):
        ans_lst[i] = ''.join([chr(num+96) for num in lst])

    for lst in ans_lst:
        print(lst)
    
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
