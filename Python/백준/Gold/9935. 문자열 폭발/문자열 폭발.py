import sys

string = sys.stdin.readline().rstrip()
C4 = sys.stdin.readline().rstrip()

stack = []
for char in string:
    stack.append(char)
    if char == C4[-1]:
        temp = "".join(stack[-len(C4):])
        if temp == C4:
            for i in range(len(C4)):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")