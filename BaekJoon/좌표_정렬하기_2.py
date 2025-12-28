import sys
input = sys.stdin.readline

# 1~100,000
N = int(input())

# 공간 복잡도 O(N)
xy_list = []

for _ in range(N):
    x,y = map(int,input().split())
    xy_list.append((x,y))

# order 1.y 2.x
xy_list.sort(key=lambda p:(p[1],p[0]))

for xy in xy_list:
    print(xy[0], xy[1])