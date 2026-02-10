import sys
sys.setrecursionlimit(10**6)
preorder = list(map(int, sys.stdin.readlines()))

def postorder(li, start_index, end_index):
    if len(li) == 0:
        return
    root = li[start_index]
    if len(li) == 1:
        print(root)
        return
    left = list()
    right = list()
    curr = start_index + 1
    while curr < end_index and root > li[curr]:
        left.append(li[curr])
        curr += 1
    while curr < end_index:
        right.append(li[curr])
        curr += 1

    postorder(left, 0, len(left))
    postorder(right, 0, len(right))
    print(root)

postorder(preorder, 0, len(preorder))