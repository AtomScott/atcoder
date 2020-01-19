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
from math import log10
# Find the first digit 
def firstDigit(n) : 
  
    # Remove last digit from number 
    # till only one digit is left 
    while n >= 10:  
        n = n / 10; 
      
    # return the first digit 
    return int(n) 
  
# Find the last digit 
def lastDigit(n) : 
  
    # return the last digit 
    return (n % 10) 

import math 
def fact(n):  
    if (n <= 1): 
        return 1
          
    return n * fact(n - 1)  
  
def nPr(n, r):  
    if n == 0:
        return 0
    if n == 1:
        return 1
    return math.floor(math.factorial(n) / math.factorial(n - r) / math.factorial(r))  

import numpy as np
from itertools import product
def count(N): 
    M = np.zeros((10, 10))
    for i in range(1, N+1):
        f = firstDigit(i)
        l = lastDigit(i)
        M[f,l] += 1

    mini = np.minimum(M, M.T)    
    f = lambda x: x * nPr(x, 2)
    m = [f(mini[i,j]) for i, j in product(range(10), range(10))]
    return int(np.sum(m))
    
# This code is contributed by Raj 
def main():
    N = int(input())
    
    print(count(N))

if __name__ == "__main__":
    main()
