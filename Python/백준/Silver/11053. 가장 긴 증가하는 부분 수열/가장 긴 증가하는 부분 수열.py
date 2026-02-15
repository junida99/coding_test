import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
for i in range(n):
    temp_length = 1
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))