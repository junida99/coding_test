import sys, heapq

n, m, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))

def dijkstra(start):
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

back = dijkstra(x)
max_time = 0
for i in range(1, n+1):
    come = dijkstra(i)
    total_time = come[x] + back[i]
    max_time = max(max_time, total_time)

print(max_time)