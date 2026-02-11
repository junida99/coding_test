import sys, time

n = int(sys.stdin.readline())
count = 0
isused_col = [False for _ in range(n)]
isused_diag1 = [False for _ in range(2*n-1)]
isused_diag2 = [False for _ in range(2*n-1)]

def dfs(row):
    global count
    if row == n:
        count += 1
        return
    for col in range(n):
        if not isused_col[col] and not isused_diag1[row + col] and not isused_diag2[row - col + ( n - 1)]:
            isused_col[col] = True
            isused_diag1[row + col] = True
            isused_diag2[row - col + (n - 1)] = True
            dfs(row + 1)
            isused_col[col] = False
            isused_diag1[row + col] = False
            isused_diag2[row - col + (n - 1)] = False
dfs(0)
print(count)