# BFS 방식으로 해쉬테이블을 하나 더 만들어 도달하는 시간 테이블을 만들어 출력
# 원하는건 최소 시간 [몇일]이기 때문에 H의 먼저오는 순서는 고려 X
# 2차원 경로구하는 방식에서 위 아래 정보가 추가된 형태
# 모든 칸에서 BFS()함수를 실행하기에 최악의 경우 100*100*100 즉 1,000,000 번 실행

# 체크리스트
# 1. 익은 토마토 체크
# 2. 비어 있는 칸 체크

# import sys
# from collections import deque

# input = sys.stdin.readline

# M, N, H = map(int, input().split())

# hash_table = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

# # print(hash_table)

# graph = []

# for _ in range(H):
#     graph.append([list(map(int,input().split())) for _ in range(N)])

# # print(graph)
# # 호출할때 H, N, M 순으로

# dx = [1,0,-1,0,0,0]
# dy = [0,-1,0,1,0,0]
# dz = [0,0,0,0,1,-1]

# def BFS(x,y,z):
#     global graph
#     global hash_table
#     global M, N, H
    
#     # 해당 BFS에서 방문했는지 체크하는 그래프 -1 미방문 0 방문
#     visit_table = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

#     if hash_table[z][y][x] is not -1 or graph[z][y][x] == -1:
#         return
#     else:
#         hash_table[z][y][x] = 0
    
#     q = deque()
#     q.append((x,y,z))
    
#     while q:
#         current = q.popleft()
#         current_day = hash_table[current[2]][current[1]][current[0]]
        
#         for x_move in dx:
#             for y_move in dy:
#                 for z_move in dz:                    
#                     next_x, next_y, next_z = current[0]+x_move, current[1]+y_move, current[2]+z_move

#                     if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N or next_z < 0 or next_z >= H:
#                         continue
                    
#                     if checker(next_x, next_y, next_z, visit_table[next_z][next_y][next_x]):
#                         visit_table[next_z][next_y][next_x] = 0 # 방문했으면 방문처리
#                         if hash_table[next_z][next_y][next_x] == -1:
#                             hash_table[next_z][next_y][next_x] = current_day+1
#                         else:
#                             hash_table[next_z][next_y][next_x] = min(current_day+1, hash_table[next_z][next_y][next_x])
#                         q.append((current[0]+x_move,current[1]+y_move,current[2]+z_move))
        

# def checker(x,y,z, vt):
#     """
#     해당 x,y,z 위치에 다음 조건 체크
#     1. 범위를 벗어났는가
#     2. 실제 있는 토마토인가
#     3. 어떤 토마토인가
#     """
#     tomato = graph[z][y][x]
#     if tomato == -1:
#         return False # 비어있는 공간
#     elif tomato == 1:
#         return False # 익은 토마토
#     elif tomato == 0 and vt == -1:
#         return True # 그냥 토마토
    

    
# for z in range(H):
#     for y in range(N):
#         for x in range(M):
#             BFS(x,y,z)


# def answer():
#     global hash_table
#     global M, N, H
#     max_trial = 0
#     for z in range(H):
#         for y in range(N):
#             for x in range(M):
#                 if hash_table[z][y][x] == -1:
#                     print(-1)
#                     return
#                 max_trial = max(hash_table[z][y][x], max_trial)
#     print(max_trial)

# print(hash_table)
   
# answer()

"""
=== 백준 7569번(토마토) 코드 리뷰 ===

[문제 이해]
- 이 문제는 3차원 창고에 보관된 토마토들이 모두 익는데 걸리는 최소 일수를 구하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O (단, 형식은 보완 필요)
- 문제 분석 단계: 보완 필요 (실행 횟수 예상은 좋으나, 연산량에 따른 시간 판단 누락)
- 자료구조 선택 근거: 명확함 (최단 시간 탐색을 위한 BFS 및 Queue 사용)
- 알고리즘 설계: 구체적
- 설계-구현 일치도: 일치

[현재 접근 방식]
- `M * N * H`의 모든 좌표를 순회하며 각각 개별적인 BFS를 실행해 `hash_table`에 도달 시간을 업데이트하고 있습니다.
- BFS 함수가 호출될 때마다 3차원 크기의 `visit_table` 배열을 매번 새로 생성하고 있습니다.

[분석 결과]
- 시간 복잡도: O((M×N×H)²) - 최악의 경우 100만 번의 반복 각각에서 최대 100만 번의 BFS 탐색 발생
- 공간 복잡도: O(M×N×H) - 반복 시마다 3차원 배열 재할당 발생
- 예상 결과: ❌ 시간초과 및 메모리 초과

[힌트]
💡 익은 토마토들은 "동시에" 상하좌우전후로 영향을 미치며 퍼져나갑니다.
- 모든 점에서 각각 BFS를 시작하지 말고, 처음부터 익어있는 토마토(1)들의 위치를 모두 찾아 **하나의 큐(Queue)에 한꺼번에 넣은 상태로 단 "한 번"의 BFS(Multi-source BFS)**를 시작해보면 어떨까요?
- BFS 수행 시 거리를 재기 위한 새로운 3차원 배열(`visit_table`, `hash_table`)을 매번 할당하지 않고, 원래 주어진 `graph` 배열 내의 값을 갱신해 나가며 며칠이 지났는지 기록하는 방식으로 공간 효율도 극대화해 볼 수 있습니다.

[설계 개선 제안]
코드 상단에 '최악의 경우 1,000,000번 실행'된다고 분석해 보신 접근 방식이 아주 훌륭합니다!
하지만 파이썬의 경우 보통 1초당 2000만 번 연산을 기준으로 하는데, 각각의 반복마다 다시 탐색하면 훨씬 더 많은 연산이 필요해집니다.
다음부터는 아래 구조를 참고해 체계적인 설계 과정을 거쳐보세요:
  1. 문제 핵심 파악
  2. 필요한 자료구조 선택
  3. 알고리즘 단계별 설명
  4. 시간/공간 복잡도 예측 (제한 시간 내 들어오는지 검증)

[더 알아보면 좋을 것]
- 다중 시작점 BFS (Multi-source BFS / 토마토가 1개 이상일 때 동시 출전 시뮬레이션)
- In-place 최적화로 3차원 배열 메모리 아끼기
"""

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int,input().split())

hash_table = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(H)]

graph = []

for _ in range(H):
    graph.append([list(map(int,input().split())) for _ in range(N)])
    
def BFS():
    """
    처음에 모든 익은 토마토를 q에 넣어서 동시에 진행
    """
    
    global M, N, H
    global graph
    global hash_table
    
    dx = [1,0,-1,0,0,0]
    dy = [0,-1,0,1,0,0]
    dz = [0,0,0,0,1,-1]
    
    q = deque()
    
    # 익은 토마토 전부 q에 넣음
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if graph[z][y][x] == 1:
                    q.append((x,y,z))
                    hash_table[z][y][x] = 0
    
    while q:
        current = q.popleft()
        
        for i in range(6):
            n_x = current[0] + dx[i]
            n_y = current[1] + dy[i]
            n_z = current[2] + dz[i]
            
            # 범위를 벗어났는지 체크
            if 0 <= n_x < M and 0 <= n_y < N and 0 <= n_z < H:
                # 토마토인지 체크
                if graph[n_z][n_y][n_x] == -1:
                    continue                
                # 이미 방문했는지 체크
                if hash_table[n_z][n_y][n_x] == -1:
                    hash_table[n_z][n_y][n_x] = hash_table[current[2]][current[1]][current[0]] + 1
                    q.append((n_x,n_y,n_z))
        
    
BFS()

result = 0
continue_work = True

# print(hash_table)

for z in range(H):
    for y in range(N):
        for x in range(M):
            if continue_work:
                check_num = hash_table[z][y][x]
                if check_num == -1 and graph[z][y][x] != -1:
                    print(-1)
                    continue_work = False
                result = max(result, check_num)

if continue_work:
    print(result)