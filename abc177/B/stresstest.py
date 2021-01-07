import sys
from random import randint

def my_solve(S, T):
    count = 1
    for s in S:
        if s in T:
            count += 1
    return count
    
def seikai_solve(S: str, T: str):
    min_change = 100000000

    S = [s for s in S]
    T = [t for t in T]

    for i, s in enumerate(S):
        for j, t in enumerate(T):
            if j == 0:
                c = 0
            if len(S) <= i + j:
                break
            if S[i+j] != t:
                c += 1
            if len(T) == j + 1:
                min_change = min(min_change, c)

    return min_change


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    while True:
        N = randint(1, 100)
        S = ''.join([chr(randint(96, 97 + 25)) for _ in range(N)])
        T = ''.join([chr(randint(97, 97 + 25)) for _ in range(N - randint(1, N))])

        seikai = seikai_solve(S, T)
        my_ans = my_solve(S,T)
        print(S, T, seikai, my_ans)
        assert seikai == my_ans

if __name__ == '__main__':
    main()