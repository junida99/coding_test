import sys
n = int(sys.stdin.readline())
stars = ["  *  ", " * * ", "*****"]
curr_k = 3
while curr_k < n:
    next_stars = []
    for s in stars:
        temp = " "*curr_k + s + " "*curr_k
        next_stars.append(temp)
    for s in stars:
        temp = s + " " + s
        next_stars.append(temp)
    stars = next_stars
    curr_k *= 2

print("\n".join(stars))