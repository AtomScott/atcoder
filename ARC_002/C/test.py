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

from itertools import product, permutations


def main():
    N = int(input())
    S = input()

    ss = ['A', 'B', 'X', 'Y']
    combs = [comb[0]+comb[1] for comb in product(ss, ss)]
    pairs = [pair for pair in permutations(combs, 2)]
    pair_count = [0 for _ in range(len(pairs))]

    for i, pair in enumerate(pairs):
        a, b = pair
        pair_count[i] = max(S.count(a) + S.replace(a,'L').count(b), S.count(b) + S.replace(b,'R').count(a))

    L, R = pairs[pair_count.index(sorted(pair_count, reverse=True)[0])]

    short_S = S.replace(L, 'L').replace(R, 'R')
    print(len(short_S))

if __name__ == "__main__":
    main()
