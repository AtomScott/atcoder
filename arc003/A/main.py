#!/usr/bin/env python3
import numpy as np

# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)

def solve(R):
    d = {
        'A':4,
        'B':3,
        'C':2,
        'D':1,
        'F':0
    }
    ans = np.mean([d[r] for r in R])

    print(ans)
    return  

def main():
    N = int(input())
    R = input()
    solve(R)
    # Failed to predict input format

if __name__ == '__main__':
    main()
