import sys

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, t, c = map(int, sys.stdin.readline().split())
house = []
cleaner = []
dust = 0
for i in range(r):
    temp = list(map(int, sys.stdin.readline().split()))
    house.append(temp)
    for j in range(t):
        if temp[j] > 0:
            dust += temp[j]
        elif temp[j] == -1:
            cleaner.append(i)

def diffusion():
    stack = []
    for i in range(r):
        for j in range(t):
            diffusion_amount = house[i][j] // 5
            total_diffustion = 0
            if diffusion_amount <= 0:
                continue
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < t and house[nx][ny] != -1:
                    stack.append((nx, ny, diffusion_amount))
                    total_diffustion += diffusion_amount
            stack.append((i, j, -total_diffustion))
    while stack:
        x, y, diff = stack.pop()
        house[x][y] += diff

def air_cleaning():
    global dust
    x1 = cleaner[0]
    for i in range(x1,0,-1):
        house[i][0] = house[i-1][0]
    for i in range(t-1):
        house[0][i] = house[0][i+1]
    for i in range(x1):
        house[i][t-1] = house[i+1][t-1]
    for i in range(t-1, 1, -1):
        house[x1][i] = house[x1][i-1]
    house[x1][1] = 0
    
    x2 = cleaner[1]
    for i in range(x2, r-1):
        house[i][0] = house[i+1][0]
    for i in range(t-1):
        house[r-1][i] = house[r-1][i+1]
    for i in range(r-1, x2, -1):
        house[i][t-1] = house[i-1][t-1]
    for i in range(t-1, 1, -1):
        house[x2][i] = house[x2][i-1]
    house[x2][1] = 0
    dust -= house[x1][0] + house[x2][0]
    house[x1][0] = -1
    house[x2][0] = -1

for i in range(c):
    diffusion()
    air_cleaning()

print(dust)