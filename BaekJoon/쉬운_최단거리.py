# https://www.acmicpc.net/problem/14940
#
# [문제 분석]
# - 목표: 지도의 모든 지점에서 목표 지점(2)까지의 거리 구하기.
# - 제약: N, M <= 1000. 시간제한 1초. O(NM) BFS 필요.
# - 입력: 0(벽), 1(땅), 2(목표지점).
# - 출력: 각 지점의 최단 거리. 
#   * 원래 갈 수 없는 땅(0) -> 0 출력
#   * 갈 수 있는데 도달 못한 땅(1) -> -1 출력
#
# [최종 코드 분석 완료]
# 1. (효율성) **최적화 완료**:
#    - 입력 루프 내에서 시작점(2) 찾기와 벽(0) 처리를 동시에 수행하여 효율적입니다.
# 2. (로직 검증) **정답 로직**:
#    - 모든 벽(0)은 `visited`가 0으로 설정됩니다.
#    - 도달 불가능한 땅(1)은 -1로 남습니다.
#    - 목표 지점(2)에서 정확히 BFS가 시작됩니다.
# 3. (성능) `sys.stdin.readline` 사용으로 대량 입력 처리에 적합합니다.

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())

graph = []
visited = [[-1] * m for _ in range(n)]

start_x, start_y = 0, 0

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

    for j in range(m):
        if row[j] == 2:
            start_x, start_y = i, j
            visited[i][j] = 0
        elif row[j] == 0:
            visited[i][j] = 0

dirx = [1,-1,0,0]
diry = [0,0,1,-1]

def bfs(s_x, s_y):    
    work_q = deque()
    work_q.append((s_x,s_y))

    while work_q:
        now_x, now_y = work_q.popleft()
        
        for i in range(4):
            next_x = now_x + dirx[i]
            next_y = now_y + diry[i]

            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue

            if graph[next_x][next_y] == 0:
                continue

            if visited[next_x][next_y] == -1:                
                visited[next_x][next_y] = visited[now_x][now_y] + 1
                work_q.append((next_x, next_y))

bfs(start_x, start_y)

for row in visited:
    print(*row)