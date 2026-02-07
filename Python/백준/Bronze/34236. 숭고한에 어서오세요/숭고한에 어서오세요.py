import sys

n = int(sys.stdin.readline())
year = list(map(int, sys.stdin.readline().split()))
d = year[1] - year[0]
print(year[-1] + d)