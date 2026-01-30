import sys

n = int(sys.stdin.readline())
down = []
max_dp = []
min_dp = []
for i in range(n):
    down.append(list(map(int, sys.stdin.readline().split())))
    if i == 0:
        max_dp.append(down[i])
    else:
        first = down[0][0] + max(max_dp[0][0], max_dp[0][1])
        second = down[0][1] + max(max_dp[0])
        third = down[0][2] + max(max_dp[0][1], max_dp[0][2])
        max_dp.pop()
        max_dp.append([first, second, third])
    if i == 0:
        min_dp.append(down[i])
    else:
        first = down[0][0] + min(min_dp[0][0], min_dp[0][1])
        second = down[0][1] + min(min_dp[0])
        third = down[0][2] + min(min_dp[0][1], min_dp[0][2])
        min_dp.pop()
        min_dp.append([first, second, third])
    down.pop()
print(max(max_dp[0]), min(min_dp[0]))