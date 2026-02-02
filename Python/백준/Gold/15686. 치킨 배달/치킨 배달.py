import sys

n, m = map(int, sys.stdin.readline().split())
chicken_point = []
house_point = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] == 2:
            chicken_point.append((i, j))
        elif temp[j] == 1:
            house_point.append((i, j))

alive_chicken = []
distance = []

def dfs(num):
    if len(alive_chicken) == m:
        temp = 0
        for i in house_point:
            nearby = float('inf')
            for j in alive_chicken:
                dist = abs(i[0] - j[0]) + abs(i[1] - j[1])
                if nearby > dist:
                    nearby = dist
            temp += nearby
        distance.append(temp)
        return
    for i in range(num, len(chicken_point)):
        alive_chicken.append(chicken_point[i])
        dfs(i+1)
        alive_chicken.pop()

dfs(0)
print(min(distance))