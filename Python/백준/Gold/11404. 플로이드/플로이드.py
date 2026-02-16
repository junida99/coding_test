import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a][b] == 0:
        graph[a][b] = c
    elif graph[a][b] > c:
        graph[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j:
                if graph[i][j] == 0:
                    if graph[i][k] != 0 and graph[k][j] != 0:
                        graph[i][j] = graph[i][k] + graph[k][j]
                elif graph[i][k] != 0 and graph[k][j] != 0 and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    print(" ".join(map(str,graph[i][1:])))