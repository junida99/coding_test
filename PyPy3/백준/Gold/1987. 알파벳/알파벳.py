import sys

r, c = map(int, sys.stdin.readline().split())
graph = []
for i in range(r):
    graph.append(sys.stdin.readline().rstrip())

alpha = [False for _ in range(26)]
alpha[ord(graph[0][0]) - ord("A")] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
deepest = 0
def dfs(graph, start, depth):
    global deepest
    if deepest < depth:
        deepest = depth
    x, y = start
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and alpha[ord(graph[nx][ny]) - ord("A")] == False:
            alpha[ord(graph[nx][ny]) - ord("A")] = True
            dfs(graph, (nx, ny), depth+1)
            alpha[ord(graph[nx][ny]) - ord("A")] = False

dfs(graph, (0,0), 1)
print(deepest)