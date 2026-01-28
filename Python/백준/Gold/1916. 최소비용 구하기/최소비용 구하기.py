import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    graph[start].append((end, weight))
start, end = map(int, sys.stdin.readline().split())


def dijkstra(start, end):
    priority_queue = []
    distance = [float('inf') for _ in range(n+1)]
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0
    while priority_queue:
        curr_cost, curr_node = heapq.heappop(priority_queue)
        if curr_cost > distance[curr_node]:
            continue
        for node in graph[curr_node]:
            total_weight = curr_cost + node[1]
            if total_weight < distance[node[0]]:
                heapq.heappush(priority_queue, (total_weight, node[0]))
                distance[node[0]] = total_weight
    return distance[end]

print(dijkstra(start, end))