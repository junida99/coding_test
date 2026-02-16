import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n+1):
    graph[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    print(" ".join(map(lambda x: str(x) if x != float('inf') else '0', graph[i][1:])))