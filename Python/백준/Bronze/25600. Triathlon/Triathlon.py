import sys

n = int(sys.stdin.readline())
max_score = 0
for i in range(n):
    a, d, g = map(int, sys.stdin.readline().split())
    if a == d+g:
        score = 2*a*(d+g)
    else:
        score = a*(d+g)
    if score > max_score:
        max_score = score

print(max_score)