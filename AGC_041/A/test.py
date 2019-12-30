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

def even(d):
    return d // 2

def odd(A, B, N):
    if abs(A-1) > abs(B-N):
        dist2edge = abs(B-N)
        A += dist2edge
        B += dist2edge 

        return even(abs((A+1)- B)) + 1 + dist2edge

    else:
        dist2edge = abs(A - 1)
        A -= dist2edge
        B -= dist2edge
    
        return even(abs(A- (B-1))) + 1 + dist2edge


def main():
    N, A, B = map(int, input().split())
    diff = abs(A-B)

    if diff % 2 == 0:
        print(even(diff))
    else:
        print(odd(A, B, N))

if __name__ == "__main__":
    main()
