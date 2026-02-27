import sys, heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
reversed_graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))
    reversed_graph[end].append((start, time))

def dijkstra(graph, start):
    priority_queue = [(0, start)]
    weight = [float('inf') for _ in range(n+1)]
    weight[start] = 0
    while priority_queue:
        w, curr = heapq.heappop(priority_queue)
        if weight[curr] < w:
            continue
        for i in graph[curr]:
            nxt, nxt_w = i
            total_w = w + nxt_w
            if weight[nxt] > total_w:
                heapq.heappush(priority_queue, (total_w, nxt))
                weight[nxt] = total_w
    return weight

come = dijkstra(reversed_graph, x)
back = dijkstra(graph, x)
max_time = 0
for i in range(1, n+1):
    max_time = max(come[i] + back[i], max_time)
print(max_time)