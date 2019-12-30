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
import numpy as np
import itertools

def main():
    N = int(input())
    d_list = []
    for i in range(N):
        d = {}
        for _ in range(int(input())):
            x, y = list(map(int, input().split()))
            d[x] = y
        d_list.append(d)


    def validate1(path, d_list):
        start_bool = path[0]
        end_bool = path[0]
        for i in range(len(path)-1):
            print(d_list, path)
            if end_bool:
                end_bool = d_list[path[i]].get(path[i+1], None)
            else:
                end_bool = not d_list[path[i]].get(path[i+1], None)
            if end_bool == None: return True
        return start_bool == end_bool
        
    def validate(d_list):
        people = list(range(N))
        for person in people:
            other_people = [other_person for other_person in people if other_person != person]
            for sub_path_len in range(1, N):
                for sub_path in itertools.combinations(other_people, sub_path_len):
                    path = [person] + list(sub_path) + [person]
                    if not validate1(path, d_list):
                        return False
        return True

    lst = [l for i in range(N+1) for l in itertools.combinations(range(N), i)]
    i = 0
    while True:
        new_d_list = d_list.copy()

        for j in lst[i]:
            new_d_list[j] = []

        if validate(d_list): 
            break
        i+= 1

if __name__ == "__main__":
    main()
