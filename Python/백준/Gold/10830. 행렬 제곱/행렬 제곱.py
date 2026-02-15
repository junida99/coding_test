import sys

n, b = map(int, sys.stdin.readline().split())
matrix = []
for i in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

def square_matrix_product(a, b):
    ans = []
    for i in range(n):
        temp = [0 for _ in range(n)]
        for j in range(n):
            for k in range(n):
                temp[k] += a[i][j] * b[j][k]
                temp[k] %= 1000
        ans.append(temp)
    return ans

def cal_squre(a, b):
    if b == 1:
        return a
    elif b % 2 == 0:
        temp = cal_squre(a, b // 2)
        return square_matrix_product(temp, temp)
    else:
        temp = cal_squre(a, b-1)
        return square_matrix_product(temp, a)

ans = cal_squre(matrix, b)
for i in range(n):
    ans[i] = map(lambda x: x % 1000, ans[i])

for i in range(n):
    print(" ".join(map(str, ans[i])))