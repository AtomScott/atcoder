import profile, pytest
import re

import sys
from io import StringIO

import sys, os
import code

import cProfile


test_data = []
for f in sorted(os.listdir('./test_samples')):
    path = os.path.join('./test_samples', f)
    if os.path.getsize(path) <= 0:
        continue
    if f.startswith('input'):
        test_data.append([path, None])
    elif f.startswith('output'):
        idx = int(re.findall(r'\d+', f)[0])
        test_data[idx][1] = path

def assertIO(input, output, fname):
    stdout, stdin = sys.stdout, sys.stdin
    sys.stdout, sys.stdin = StringIO(), StringIO(input)
    
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    pr.dump_stats(os.path.join('./prof/', os.path.split(fname)[1]+'.prof'))

    sys.stdout.seek(0)
    out = sys.stdout.read()[:-1]
    sys.stdout, sys.stdin = stdout, stdin
    if output == '?':
        assert True
    else:
        assert out == output
    
@pytest.mark.parametrize('in_file, out_file', test_data)
def test_compute(in_file, out_file):
    with open(in_file, 'r') as file:
        input = file.read()
    with open(out_file, 'r') as file:
        output = file.read()
    assertIO(input, output, in_file)

               
################################################
# Start Below

# imports    
from itertools import accumulate, permutations

def solve_patterns(X, As, acc, N):
    n_patterns = 0
    for a in As:
        if acc[-1] >= X - (a * N):
            n_patterns += N
        else:
            i = 0
            while acc[i] >=  X - (a * i):
                print(acc[i], end=' ')
                n_patterns += 1
    return n_patterns

def main():
    
    N, M = map(int, input().split())
    As = list(map(int, input().split()))

    As.sort(reverse=True)
    acc = [0] + list(accumulate(As))
    
    for i in range(sum([a+b for a, b in permutations(As,2)])):
        print(i, solve_patterns(i, As, acc, N))

    l, r = 0, 2**N
    m = (l+r)//2
    X = solve_patterns(m, As, acc, N)
    i = 0 

    while M != X:
        m = (l+r)//2
        X = solve_patterns(m, As, acc, N)
        if X >= M:
            r = X - 1
        else:
            l = X + 1
        print(X, m)

        i += 1
        if i ==10:
            break

        
    print(cum)

if __name__ == "__main__":
    main()
