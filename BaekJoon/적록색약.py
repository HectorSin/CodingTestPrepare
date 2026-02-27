# 적록 색약이 보는 공간 나타내는 문제
# 사실 두가지 버전의 BFS를 돌리면 해결 자체는 가능해 보임 [but 시간제한 문제]
# 정사각형이고 100*100 = 10000가지의 케이스
# 케이스가 적어 두가지 방식 적용 가능해 보임

# 1. 우선 방문했는지 체크
# 2. 무슨 색인지 체크

# 1. 큐에 현재 위치 넣기
# 2. 큐에서 1개 빼기
# 3. 다음 위치 4개 찾기
# 4. 범위 벗어났는지 체크
# 5. 방문했었는지 체크
# 6. 같은 색인지 체크

import sys
input = sys.stdin.readline

from collections import deque

def base_BFS(row,col):
    """
    일반인이 보는 지역
    """
    global nor_num
    global graph, next_col, next_row, visited_list
    
    if visited_list[row][col] == 1:
        return
    color = graph[row][col]
    nor_num += 1
    
    q = deque()
    q.append((row,col))
    
    visited_list[row][col] = 1
    
    while q:
        current = q.popleft()
        
        for i in range(4):
            n_row = current[0] + next_row[i]
            n_col = current[1] + next_col[i]
            
            if 0 <= n_row < N and 0 <= n_col < N:
                if visited_list[n_row][n_col] != 1:
                    if graph[n_row][n_col] == color:
                        visited_list[n_row][n_col] = 1
                        q.append((n_row,n_col))
            
    
def seg_BFS(row,col):
    """
    색맹이 보는 지역
    
    Blue 면 Blue
    아니면 Else
    """
    global seg_num
    global graph, next_col, next_row, visited_list
    
    if visited_list[row][col] == 1:
        return
    
    if graph[row][col] == "B":
        color = "Blue"
    else:
        color = "Else"
    
    seg_num += 1
    
    q = deque()
    q.append((row,col))
    
    visited_list[row][col] = 1
    
    while q:
        current = q.popleft()
        
        for i in range(4):
            n_row = current[0] + next_row[i]
            n_col = current[1] + next_col[i]
            
            if 0 <= n_row < N and 0 <= n_col < N:
                if visited_list[n_row][n_col] != 1:
                    if graph[n_row][n_col] == "B":
                        n_color = "Blue"
                    else:
                        n_color = "Else"
                    if n_color == color:
                        visited_list[n_row][n_col] = 1
                        q.append((n_row,n_col))

N = int(input())

graph = [] # 지도

for _ in range(N):
    graph.append(list(input().rstrip()))
    
nor_num = 0 # 일반 그룹
seg_num = 0 # 색맹 그룹

next_row = [1,0,-1,0]
next_col = [0,-1,0,1]

visited_list = [[0] * N for _ in range(N)]
# print(visited_list[4][4])

for row in range(N):
    for col in range(N):
        base_BFS(row,col)

# print(nor_num)

visited_list = [[0] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        seg_BFS(row,col)

# print(seg_num)

print(nor_num, seg_num)