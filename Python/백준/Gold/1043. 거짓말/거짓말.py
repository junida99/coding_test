import sys

n, m = map(int, sys.stdin.readline().split())
truth_init = list(map(int, sys.stdin.readline().split()))
parties = []

parent = [i for i in range(n+1)]
truth_set = set()
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    
    if rootA != rootB:
        parent[rootB] = rootA

for i in range(m):
    party = list(map(int, sys.stdin.readline().split()))
    if party[0] > 1:
        for j in range(2, party[0]+1):
            union(party[j], party[j-1])
    parties.append(party)

for i in range(1, truth_init[0]+1):
    truth_init[i] = find(truth_init[i])
    truth_set.add(truth_init[i])

lie = m
for party in parties:
    for i in range(1, party[0]+1):
        if find(party[i]) in truth_set:
            lie -= 1
            break
print(lie)