import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            if dp[i+1][j] > dp[i][j+1]:
                dp[i+1][j+1] = dp[i+1][j]
            else:
                dp[i+1][j+1] = dp[i][j+1]

print(dp[len(b)][len(a)])