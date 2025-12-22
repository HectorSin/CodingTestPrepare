# 세변 input -> 직각삼각형 여부 print

while True:
    lines = sorted(list(map(int,input().split())))
    
    if sum(lines) == 0:
        break

    if (lines[0] ** 2) + (lines[1] ** 2) == (lines[2] ** 2):
        print("right")
    else:
        print("wrong")