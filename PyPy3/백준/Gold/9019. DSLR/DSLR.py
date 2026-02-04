import sys
from collections import deque
def left_rotate(string):
    return string[1] + string[2] + string[3] + string[0]
def right_rotate(string):
    return string[3] + string[0] + string[1] + string[2]
def bfs(startval, endval):
    visited = set()
    queue = deque()
    queue.append((startval, ""))
    while queue[0][0] != endval:
        curr = queue.popleft()
        strcurr = str(curr[0])
        while len(strcurr) < 4:
            strcurr = "0" + strcurr
        d = (curr[0] * 2) % 10000
        if curr[0] == 0:
            s = 9999
        else:
            s = curr[0] - 1
        l = int(left_rotate(strcurr))
        r = int(right_rotate(strcurr))
        if d not in visited:
            queue.append((d, curr[1]+"D"))
            visited.add(d)
        if s not in visited:
            queue.append((s, curr[1]+"S"))
            visited.add(s)
        if l not in visited:
            queue.append((l, curr[1]+"L"))
            visited.add(l)
        if r not in visited:
            queue.append((r, curr[1]+"R"))
            visited.add(r)
    return queue.popleft()[1]

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(a, b))