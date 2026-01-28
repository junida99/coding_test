import sys

n, m = map(int, sys.stdin.readline().split())
sheet = []
prefix_sum = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    sheet.append(temp)
    for j in range(1,n):
        temp[j] = temp[j] + temp[j-1]
    prefix_sum.append(temp)
for i in range(1, n):
    for j in range(n):
        prefix_sum[i][j] = prefix_sum[i][j] + prefix_sum[i-1][j]

for i in range(m):
    x1, x2, y1, y2 = map(lambda x:int(x)-1, sys.stdin.readline().split())
    if x1 != 0 and x2 != 0:
        ans = prefix_sum[y1][y2] - prefix_sum[x1-1][y2] - prefix_sum[y1][x2-1] + prefix_sum[x1-1][x2-1]
    elif x1 == 0 and x2 != 0:
        ans = prefix_sum[y1][y2] - prefix_sum[y1][x2-1]
    elif x1 != 0 and x2 == 0:
        ans = prefix_sum[y1][y2] - prefix_sum[x1-1][y2]
    else:
        ans = prefix_sum[y1][y2]
    print(ans)