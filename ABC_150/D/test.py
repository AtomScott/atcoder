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
import bisect
import numpy as np
from operator import mul
from functools import reduce

def get_prime_factors(num):
    primes, i = [], 1
    while num >= i >= 1:
        if num % i == 0:
            primes.append(i)
            num /= i
        i += 1
    return primes

def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    lst = None
    primes = [ ]
    for a in A:
        diff = np.setdiff1d(get_prime_factors(a), primes)
        if diff.size==0:
            continue
        else:
            primes = np.append(primes, diff)

    num = reduce(mul, primes, 1)

    Xs = []
    if a % 2 == 0:
        P = M // int(num)
        for p in range(P):
            x = (p + 0.5) * num    

            if x not in Xs:
                Xs.append(x)
        if lst is None:
            lst = Xs
        else:
            lst = np.intersect1d(lst, Xs)
    else:
        pass
        
    print(len(lst), lst)


if __name__ == "__main__":
    main()
    # print(get_prime_factors(int(input())))
