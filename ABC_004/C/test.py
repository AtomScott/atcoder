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


import itertools

def switch(S, i):
    S[i%5], S[i%5+1] = S[i%5+1], S[i%5]
    return S

d = {}    
def main():
    N = int(input())
    S = [i for i in range(1,6+1)]

    for i in range(6):
        for comb in itertools.permutations(S, 6):
            comb = list(comb)
            key = str(i)+''.join(map(str,comb))
            d[key] = switch(comb, i)

    untouched_S = S
    for i in range(N):
        if S == untouched_S and i != 0:
            cycle_len = i
            S = untouched_S

            for i in range(N%cycle_len):
                key = str(i%5)+''.join(map(str,S))
                S = d[key]

            break
        key = str(i%5)+''.join(map(str,S))
        S = d[key]
    



    print(''.join(map(str,S)))

if __name__ == "__main__":
    main()
