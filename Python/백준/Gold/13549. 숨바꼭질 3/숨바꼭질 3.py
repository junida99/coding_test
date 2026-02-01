import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
distance = [float('inf') for _ in range(1000001)]
priority_queue = [(0, n)]
while priority_queue:
    total_weight, point = heapq.heappop(priority_queue)
    if point >= k:
        if distance[k] > total_weight + (point - k):
            total_weight += point - k
            heapq.heappush(priority_queue, (total_weight, k))
            distance[k] = total_weight
    else:
        if distance[point - 1] > total_weight + 1 and point - 1 > -1:
            heapq.heappush(priority_queue, (total_weight+1, point-1))
            distance[point - 1] = total_weight + 1
        if distance[point + 1] > total_weight + 1:
            heapq.heappush(priority_queue, (total_weight+1, point+1))
            distance[point + 1] = total_weight + 1
        if distance[2*point] > total_weight:
            heapq.heappush(priority_queue, (total_weight, 2*point))
            distance[2*point] = total_weight
print(distance[k])