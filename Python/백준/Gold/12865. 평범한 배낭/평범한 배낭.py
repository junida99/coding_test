import sys
n, k = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(k+1)]]
for i in range(1, n+1):
    w, v = map(int, sys.stdin.readline().split())
    temp = [0 for _ in range(k+1)]
    for j in range(1, k+1):
        if w <= j:
            temp[j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            temp[j] = dp[i-1][j]
    dp.append(temp)
print(dp[n][k])