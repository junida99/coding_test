import sys

string = sys.stdin.readlines()
for case in string:
    a, b, c = map(int, case.split())
    diff_ab = abs(a-b)
    diff_bc = abs(b-c)
    if diff_ab > diff_bc:
        print(abs(a-b)-1)
    else:
        print(abs(b-c)-1)