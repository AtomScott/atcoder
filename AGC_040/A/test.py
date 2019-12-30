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

def left(arr, idx):
    if L[idx] != None:
        return L[idx]

    if arr[idx] == '<':
        if idx == 0:
            ret = 1
        else:
            ret = left(arr, idx-1) + 1
    else:
        ret = 0

    L[idx] = ret
    return ret
        
def right(arr, idx):
    if R[idx] != None:
        return R[idx]

    if arr[idx] == '>':    
        if idx == len(arr)-1:
            ret =  1
        else:
            ret = right(arr, idx+1) + 1
    else:
        ret = 0
    R[idx] = ret
    return ret

def main():
    S = list(input())
    N = len(S)
    A = [0 for _ in range(N+1)]
    
    global L; L = [None for _ in range(N)]
    global R; R = [None for _ in range(N)]

    for i in range(N):
        j = N - i - 1
        L[i] = left(S, i)
        R[j] = right(S, j)
    
    L = [0] + L
    R = R + [0]

    for i in range(len(A)):
        A[i] = max(L[i], R[i])
            
    print(sum(A))

if __name__ == "__main__":
    main()
