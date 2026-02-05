import sys

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

chicken = a // 2 + b
if chicken > n:
    print(n)
else:
    print(chicken)