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
from itertools import combinations
import operator as op
from functools import reduce


def ncr(n, r, fac):
    return fac[n] / fac[r] / fac[n-r] 

def main():

    N, K = list(map(int,input().split()))
    As = list(map(int,input().split()))
    As. sort()
    
    mod = 10**9 +7
    fac = [1]
    for i in range(1, N):
        fac.append(fac[i-1]*i)

    s = 0
    for i in range(N):
        for j in range(i+K-1, N):
            # print(i, j, (As[j] - As[i]) , ncr(j-i-1, K-2), ncr(2, 3))
            s += (As[j] - As[i]) * ncr(j-i-1, K-2, fac)

   # combs = combinations(range(N), K)
    # for tup in combs:
    #     mn_idx = tup[0]
    #     mx_idx = tup[-1]

    #     s +=  As[mx_idx] - As[mn_idx] 

    print(int(s%mod))

if __name__ == "__main__":
    main()
