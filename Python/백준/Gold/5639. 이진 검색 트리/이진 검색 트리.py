import sys
sys.setrecursionlimit(20000)

preorder = list(map(int, sys.stdin.readlines()))

def postorder(start, end):
    if start >= end:
        return
    
    root = preorder[start]
    mid = end
    for idx in range(start+1, end):
        if preorder[idx] > root:
            mid = idx
            break
    
    postorder(start+1, mid)
    postorder(mid, end)
    print(root)

postorder(0, len(preorder))