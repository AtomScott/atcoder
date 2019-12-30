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
def points(me, you, R, S, P):
    hand_map = {
        'r':'p',
        's':'r',
        'p':'s'
    }
    if hand_map[you] == me:
        if me == 'r':
            return R
        elif me =='p':
            return P
        elif me =='s':
            return S
    else:
        return 0
    
def main():
    N, K = list(map(int, input().split()))
    R, S, P = list(map(int, input().split()))
    T = input()
    Ts = list(T)

    hand_map = {
        'r':'p',
        's':'r',
        'p':'s'
    }

    memo = []
    cum = 0
    for i, t in enumerate(Ts):
        hand = hand_map[t]
        
        if i >= K:
            if hand == memo[i - K]:
                hand = 'na'
            

        memo.append(hand)
        cum += points(hand, t, R, S, P)
        # print(cum, i, t, memo)


    print(cum)

if __name__ == "__main__":
    main()
