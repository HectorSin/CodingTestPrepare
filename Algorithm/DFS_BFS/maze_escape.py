"""
미로탈출
"""
from collections import deque

N, M = map(int,input().split())

graph = []

for i in range(N):
    graph.append(list(map(int,input())))

# 이동할 방향들 지정
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        # 4방향으로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 좌표가 미로 밖이면 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            # 다음 좌표가 벽이면 무시
            if graph[nx][ny] == 0:
                continue

            # 들르지 않은 장소이면 거리 계산 진행
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[N-1][M-1]

print(BFS(0,0))