import sys, heapq

n, e = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(graph, start, end):
    weight_list = [float("inf") for i in range(n+1)]
    priority_queue = [(0, start)]
    weight_list[start] = 0
    while priority_queue:
        curr_weight, curr = heapq.heappop(priority_queue)
        if curr_weight > weight_list[curr]:
            continue
        for node, weight in graph[curr]:
            total_weight = curr_weight + weight
            if total_weight < weight_list[node]:
                weight_list[node] = total_weight
                heapq.heappush(priority_queue, (total_weight, node))
    return weight_list[end]

first = dijkstra(graph, 1, v1) + dijkstra(graph, v1, v2) + dijkstra(graph, v2, n)
second = dijkstra(graph, 1, v2) + dijkstra(graph, v2, v1) + dijkstra(graph, v1, n)
ans = min(first, second)
if ans == float('inf'):
    print(-1)
else:
    print(ans)