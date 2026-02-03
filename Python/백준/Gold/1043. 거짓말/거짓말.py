import sys

n, m = map(int, sys.stdin.readline().split())
truth_init = list(map(int, sys.stdin.readline().split()))
truth_final = set()
parties = []
graph = [set() for _ in range(n+1)]
# graph 생성
for i in range(m):
    party = list(map(int, sys.stdin.readline().split()))
    for j in range(1, party[0]+1):
        for k in range(1, party[0]+1):
            graph[party[j]].add(party[k])
    parties.append(party)

# DFS 정의
def dfs(graph, start):
    stack = [start]
    visited = [False for _ in range(n+1)]
    truth_final.add(start)
    visited[start] = True
    while stack:
        curr = stack.pop()
        for person in graph[curr]:
            if visited[person] == False:
                stack.append(person)
                visited[person] = True
                truth_final.add(person)

# 진실을 최종적으로 아는 사람 탐색
for i in range(1, truth_init[0]+1):
    dfs(graph, truth_init[i])

# 거짓말 해도 되는 파티 계산
truth = 0
for party in parties:
    for i in range(1, party[0]+1):
        if party[i] in truth_final:
            truth += 1
            break
print(m-truth)