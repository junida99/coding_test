import sys

n = int(sys.stdin.readline())
price = int(sys.stdin.readline())
for i in range(n-1):
    diff = int(sys.stdin.readline())
    price += diff

print(price)