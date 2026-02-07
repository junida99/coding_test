import sys
sys.setrecursionlimit(100000)
n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, w = map(int, sys.stdin.readline().split())
    tree[a].append((b, w))
    tree[b].append((a, w))

visited = [False for _ in range(n+1)]
visited[1] = True
deepest = 0
distance = 0
diameter_point  = 1
def dfs(graph, start):
    global deepest, distance, diameter_point
    leaf = True
    temp = graph[start]
    for node in temp:
        if visited[node[0]] == False:
            leaf = False
            distance += node[1]
            visited[node[0]] = True
            dfs(graph, node[0])
            distance -= node[1]
    if leaf == True and distance > deepest:
        deepest = distance
        diameter_point = start

dfs(tree, 1)
visited = [False for _ in range(n+1)]
visited[diameter_point] = True
distance = 0
deepest = 0
dfs(tree, diameter_point)
print(deepest)