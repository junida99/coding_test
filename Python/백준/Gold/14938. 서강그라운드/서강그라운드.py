import sys, heapq

n, m ,r = map(int, sys.stdin.readline().split())
area_item = list(map(int, sys.stdin.readline().split()))
sogang_ground = [[] for _ in range(n+1)]
for i in range(r):
    a, b, l = map(int, sys.stdin.readline().split())
    sogang_ground[a].append((b, l))
    sogang_ground[b].append((a, l))

def dijkstra(start):
    distance = [float('inf') for _ in range(n+1)]
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0
    while priority_queue:
        curr_w, curr = heapq.heappop(priority_queue)
        if curr_w > distance[curr]:
            continue
        for next_a, weight in sogang_ground[curr]:
            next_distance = curr_w + weight
            if next_distance < distance[next_a]:
                heapq.heappush(priority_queue, (next_distance, next_a))
                distance[next_a] = next_distance
    return distance

max_item = 0
for i in range(1,n+1):
    distance = dijkstra(i)
    item = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            item += area_item[i-1]
    max_item = max(max_item, item)

print(max_item)