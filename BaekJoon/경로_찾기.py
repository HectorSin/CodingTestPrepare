import sys
from collections import deque
input = sys.stdin.readline

# Baekjoon 11403: 경로 찾기
# https://www.acmicpc.net/problem/11403
# 문제: 가중치 없는 방향 그래프 G에서 모든 정점 (i, j)에 대해 i -> j 경로 유무 구하기
# 해결: BFS 탐색 (visit 배열을 이용한 O(N^3) 풀이)
n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

def BFS(array, i):
    queue = deque()
    queue.append(i)
    visit = [0] * n

    while queue:
        current = queue.popleft()

        for h in range(n):
            if array[current][h] == 1:
                if visit[h] == 0:
                    visit[h] = 1
                    queue.append(h)
    
    return visit
    
for h in range(n):
    visit_list = BFS(graph, h)
    print(*visit_list)