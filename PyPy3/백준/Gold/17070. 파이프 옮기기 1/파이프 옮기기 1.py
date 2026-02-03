import sys

n = int(sys.stdin.readline())
house = []
for i in range(n):
    house_temp = list(map(int, sys.stdin.readline().split()))
    house_temp.append(1)
    house.append(house_temp)
house_temp = [1 for _ in range(n+1)]
house.append(house_temp)

count = 0
def dfs(point, direction):
    global count
    x, y = point
    if point == (n-1, n-1):
        count += 1 
        return
    if direction == -1:
        if house[x][y+1] == 0:
            dfs((x, y+1), -1)
            if house[x+1][y] == 0 and house[x+1][y+1] == 0:
                dfs((x+1, y+1), 0)
    elif direction == 0:
        if house[x][y+1] == 0:
            dfs((x, y+1), -1)
            if house[x+1][y] == 0 and house[x+1][y+1] == 0:
                dfs((x+1, y+1), 0)
        if house[x+1][y] == 0:
            dfs((x+1, y), 1)
    elif direction == 1:
        if house[x+1][y] == 0:
            dfs((x+1, y), 1)
            if house[x][y+1] == 0 and house[x+1][y+1] == 0:
                dfs((x+1, y+1), 0)

dfs((0, 1), -1)
print(count)