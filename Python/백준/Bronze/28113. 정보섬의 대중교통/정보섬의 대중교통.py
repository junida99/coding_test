import sys

n, a, b = map(int, sys.stdin.readline().split())

if n > b:
    print("Bus")
elif a < b:
    print("Bus")
elif a > b:
    print("Subway")
elif a == b:
    print("Anything")