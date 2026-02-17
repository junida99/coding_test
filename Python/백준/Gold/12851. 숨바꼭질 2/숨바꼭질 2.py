from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())
visited = [[float('inf'), 0] for _ in range(100001)]

def bfs(start, target):
    queue = deque()
    queue.append(start)
    visited[start] = [0, 1]
    while queue:
        curr = queue.popleft()
        if curr == target:
            break
        if curr+1 <= target and visited[curr+1][0] >= visited[curr][0] + 1 :
            queue.append(curr+1)
            visited[curr+1][0] = visited[curr][0] + 1
            visited[curr+1][1] += 1
        if curr-1 >= 0 and visited[curr-1][0] >= visited[curr][0] + 1:
            queue.append(curr-1)
            visited[curr-1][0] = visited[curr][0] + 1
            visited[curr-1][1] += 1
        if 2*curr < 2*target and 2*curr <= 100000 and visited[2*curr][0] >= visited[curr][0] + 1:
            queue.append(2*curr)
            visited[2*curr][0] = visited[curr][0] + 1
            visited[2*curr][1] += 1

bfs(n, k)
print(visited[k][0])
print(visited[k][1])