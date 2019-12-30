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

import math
# Calculate amount of water that won't oveflow
def calc(a,b,deg): 
    
    rad = math.radians(deg)

    if b*math.tan(math.pi/2-rad) <= a:
        total_area = (b*math.tan(math.pi/2-rad)*b*1/2)
    if b*math.tan(math.pi/2-rad)>a:
        total_area = (a*b - a*math.tan(rad)*a*1/2)       

    return total_area * a

import bisect
def main():
    a, b, x = list(map(int, input().split()))

    left = 0
    right = 90
    deg = 45
    while True:
        y = calc(a, b, deg)
        if y - x >= -10 ** -7 and y - x <= 0:
            break
        if y > x:
            deg, left = (right+deg)/2, deg
        elif y < x:
            deg, right = (left+deg)/2, deg
    print(deg)

if __name__ == "__main__":
    main()
