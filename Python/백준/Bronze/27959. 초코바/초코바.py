import sys

n, m = map(int, sys.stdin.readline().split())
n *= 100
if n >= m:
    print("Yes")
else:
    print("No")