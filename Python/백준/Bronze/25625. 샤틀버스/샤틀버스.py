import sys
x, y = map(int, sys.stdin.readline().split())

if x > y:
    print(x+y)
else:
    print(y-x)