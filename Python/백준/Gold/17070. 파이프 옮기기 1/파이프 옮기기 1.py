import sys

n = int(sys.stdin.readline())
house = []
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
for i in range(n):
    house_temp = list(map(int, sys.stdin.readline().split()))
    #house_temp.append(1)
    house.append(house_temp)
#house_temp = [1 for _ in range(n+1)]
#house.append(house_temp)

dp[0][1][0] = 1
for i in range(2, n):
    if house[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]
for i in range(1, n):
    for j in range(1, n):
        if house[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            if house[i-1][j] == 0 and house[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
print(sum(dp[n-1][n-1]))