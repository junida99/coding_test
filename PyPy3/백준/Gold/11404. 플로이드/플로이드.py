import sys, heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for i in range(m):
    # a: 출발도시, b: 도착도시, c:cost
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

def dijkstra(start):
    total_cost = [float("Inf") for _ in range(n+1)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    total_cost[start] = 0
    while priority_queue:
        cost, curr = heapq.heappop(priority_queue)
        for next_city, next_cost in graph[curr]:
            temp_cost = cost + next_cost
            if temp_cost < total_cost[next_city]:
                heapq.heappush(priority_queue, (temp_cost, next_city))
                total_cost[next_city] = temp_cost
    return_val = []
    for i in range(1, n+1):
        if total_cost[i] == float("Inf"):
            return_val.append(0)
        else:
            return_val.append(total_cost[i])
    return return_val

for i in range(1, n+1):
    print(" ".join(map(str,dijkstra(i))))