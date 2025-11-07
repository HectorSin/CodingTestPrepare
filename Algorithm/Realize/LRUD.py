# 상하좌우

N = int(input())

direction = list(input().split())

now = [1,1]

for dir in direction:
    if dir == "R":
        if now[1] == N:
            pass
        else:
            now[1] += 1
    elif dir == "U":
        if now[0] == 1:
            pass
        else:
            now[0] -= 1
    elif dir == "L":
        if now[1] == 1:
            pass
        else:
            now[1] -= 1
    elif dir == "D":
        if now[0] == N:
            pass
        else:
            now[0] += 1

print(now[0],now[1])