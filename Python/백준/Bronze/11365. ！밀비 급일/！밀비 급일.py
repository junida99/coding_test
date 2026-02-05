import sys

while True:
    cryto = sys.stdin.readline().rstrip()
    if cryto == "END":
        break
    temp = []
    for i in range(len(cryto)-1, -1, -1):
        temp.append(cryto[i])
    print("".join(temp))