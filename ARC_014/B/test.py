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


def main():
    N = int(input())
    S = [input() for _ in range(N)]


    mem = {}
    result = False
    for i in range(N-1):
        if mem.get(S[i], False):
            break
        elif S[i][-1] != S[i+1][0]:
            i += 1
            break
        elif i == N-2:
            i = -1
            break
        mem[S[i]] = True

    if N <= 1:
        print('DRAW')
    elif i == -1:
        print('DRAW')
    elif i % 2 == 0:
        print('LOSE')
    elif i % 2 == 1:
        print('WIN')


if __name__ == "__main__":
    main()
