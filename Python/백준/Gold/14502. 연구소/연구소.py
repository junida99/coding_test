'''
Docstring for CLASS 4.14502-연구소
브루트포스 경우의 수 ~ n^3 (컴비네이션)
완전탐색 ~ n (dfs)
n^4
'''

import sys

n, m = map(int, sys.stdin.readline().split())
lab = []
able_wall = []
virus_point = []
safe_area = 0
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if temp[j] == 0:
            safe_area += 1
            able_wall.append((i,j))
        elif temp[j] == 2:
            virus_point.append((i,j))
    lab.append(temp)

def dfs(points:list, safe_count:int, wall:list):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    safe_count -= 3
    for point in wall:
        x, y = point
        lab[x][y] = 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    stack = []
    for point in points:
        stack.append(point)
        x, y  = point
        visited[x][y] = True
    
    while stack:
        curr_x, curr_y = stack.pop()
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] is False and lab[nx][ny] == 0:
                visited[nx][ny] = True
                stack.append((nx, ny))
                safe_count -= 1
    
    for point in wall:
        x, y = point
        lab[x][y] = 0

    return safe_count

ans = 0
possibility = []
def backtracking(start):
    global ans
    if len(possibility) == 3:
        safe_count = dfs(virus_point, safe_area, possibility)
        ans = max(ans, safe_count)
        return
    
    for i in range(start, len(able_wall)):
        possibility.append(able_wall[i])
        backtracking(i+1)
        possibility.pop()

backtracking(0)
print(ans)