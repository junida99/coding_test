import sys

a, b = map(int, sys.stdin.readline().split())
k, x = map(int, sys.stdin.readline().split())

start = k - x
end = k + x
if start < a:
    start = a
if end > b:
    end = b
if start > end:
    print("IMPOSSIBLE")
else:
    print(end - start + 1)