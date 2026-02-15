import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

dp_rev = [1 for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n-1, i,-1):
        if a[i] > a[j]:
            dp_rev[i] = max(dp_rev[i], dp_rev[j] + 1)

for i in range(n):
    dp[i] += dp_rev[i] - 1

print(max(dp))