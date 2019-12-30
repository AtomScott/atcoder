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
def sumXOR( arr,  n): 
    sum = 0
    for i in range(0, 64): 
        zc = 0
        oc = 0
        idsum = 0
        for j in range(0, n): 
            if (arr[j] % 2 == 0): 
                zc = zc + 1
            else: 
                oc = oc + 1
            arr[j] = int(arr[j] / 2) 
        idsum = oc * zc * (1 << i) 
        sum = sum + idsum;        
    return sum
  
def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = sumXOR(A, len(A))
    print(count%(10**9+7))

if __name__ == "__main__":
    main()
