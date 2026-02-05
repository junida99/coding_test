import sys, heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, w = map(int, sys.stdin.readline().split())
    graph[a].append((b, w))

def dijkstra(graph, start):
    weight = [float('inf') for _ in range(v+1)]
    priority_queue = [(0, start)]
    weight[start] = 0
    while priority_queue:
        curr_w, curr = heapq.heappop(priority_queue)
        if curr_w > weight[curr]:
            continue
        for next_v, distance in graph[curr]:
            next_w = curr_w + distance
            if next_w < weight[next_v]:
                heapq.heappush(priority_queue, (next_w, next_v))
                weight[next_v] = next_w
    return weight

ans = dijkstra(graph,k)
for i in range(1, v+1):
    if ans[i] == float('inf'):
        print("INF")
    else:
        print(ans[i])