# 문제: 백준 11650번 좌표 정렬하기 (https://www.acmicpc.net/problem/11650)
# 목표: 2차원 평면 위의 점을 x좌표 증가하는 순, x가 같으면 y좌표 증가하는 순서로 정렬
# 시간 복잡도: O(N log N) (N <= 100,000, 1초 제한 통과 가능)

import sys
input = sys.stdin.readline

N = int(input())

# 공간 복잡도 O(N)
xy_list = []

for i in range(N):
    # x,y는 -100,000~100,000
    x,y = map(int,input().split())
    xy_list.append((x,y))

# [정렬 Tip] 파이썬의 튜플 비교 규칙은 기본적으로 첫 번째 원소부터 순차적으로 비교합니다.
# 따라서 key를 지정하지 않고 xy_list.sort()만 해도 (x, y) 순서로 오름차순 정렬됩니다.
# 현재 작성하신 key=lambda p: (p[0], p[1])도 명시적이라서 좋습니다.
xy_list.sort(key=lambda p: (p[0], p[1]))

for xy in xy_list:
    print(xy[0], xy[1])
