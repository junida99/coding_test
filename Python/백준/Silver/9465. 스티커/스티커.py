import sys
t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    sticker = []
    sticker.append(list(map(int, sys.stdin.readline().split())))
    sticker.append(list(map(int, sys.stdin.readline().split())))
    dp = [[sticker[0][0]], [sticker[1][0]]]
    
    for j in range(1, n):
        if j == 1:
            dp[0].append(sticker[0][j] + dp[1][j-1])
            dp[1].append(sticker[1][j] + dp[0][j-1])
        else:
            dp[0].append(max(sticker[0][j] + dp[1][j-1], sticker[0][j] + dp[1][j-2]))
            dp[1].append(max(sticker[1][j] + dp[0][j-1], sticker[1][j] + dp[0][j-2]))
    print(max(dp[0][n-1], dp[1][n-1]))