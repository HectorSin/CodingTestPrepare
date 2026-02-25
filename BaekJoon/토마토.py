# 백준 7576번 토마토 문제

# M,N 2~1000
# BFS 방식으로 접근 필요
# 동시다발적으로 진행이 되기에 처음에 모든 익은 토마토들을 큐에 넣고 진행
# 1. 큐에서 토마토 꺼내기
# 2. 4가지 방향으로 다음 위치 구하기
# 3. 다음 위치 조건 구하기 [범위를 벗었는가, 토마토인가, 이미 익은 토마토인가]
# 4. 조건에 통과하면 몇일 걸렸는지 해쉬테이블에 저장하고 스택에 넣기

import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

# print(graph)
# graph[N][M]

hash_table = [[0] * M for _ in range(N)]

# print(hash_table)

q = deque()

def BFS():
    """
    BFS 방식의 알고리즘
    """
    global q
    
    next_m = [1,0,-1,0]
    next_n = [0,-1,0,1]
    
    while q:
        current = q.popleft()
        
        for i in range(4):
            n_n = current[0] + next_n[i]
            n_m = current[1] + next_m[i]
            
            if 0 <= n_n < N and 0 <= n_m < M:
                if graph[n_n][n_m] == 0 and hash_table[n_n][n_m] == 0:
                    q.append((n_n,n_m))
                    hash_table[n_n][n_m] = hash_table[current[0]][current[1]] + 1
        
        

for n in range(N):
    for m in range(M):
        if graph[n][m] == 1:
            q.append((n,m))

# print(q)

BFS()

def find_answer(N,M):
    global hash_table
    max_day = 0
    
    for n in range(N):
        for m in range(M):
            if graph[n][m] != -1:
                if hash_table[n][m] == 0 and graph[n][m] != 1:
                    return -1
                max_day = max(max_day, hash_table[n][m])
    return max_day

print(find_answer(N,M))

"""
=== 백준 7576번 코드 리뷰 ===

[문제 이해]
- 창고에 보관된 토마토들이 익어가는 과정을 시뮬레이션하여 모든 토마토가 익는데 걸리는 최소 일수를 구하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O
- 문제 분석 단계: 충분함 (동시다발적 진행의 특징을 잘 파악)
- 자료구조 선택 근거: 명확함
- 알고리즘 설계: 구체적
- 설계-구현 일치도: 일치 (단, 설계 주석 4번의 '스택에 넣기'는 실제 구현에서 '큐에 넣기'로 알맞게 작성하셨습니다)

[현재 접근 방식]
- BFS를 활용해 초기에 익은 모든 토마토를 큐에 넣고 동시 탐색을 진행하며, `hash_table` 배열에 익는데 걸리는 일수를 기록하는 방식을 사용하고 있습니다.

[분석 결과]
- 시간 복잡도: O(N × M)
- 공간 복잡도: O(N × M)
- 예상 결과: 통과

[힌트]
💡 완벽하게 잘 해결하셨습니다!
- 다중 출발점 BFS의 핵심 아이디어인 "모든 시작점을 큐에 먼저 넣고 BFS 수행"을 아주 정확하게 파악하고 구현하셨습니다. 설계부터 구현까지 흐름이 아주 좋습니다.

[더 알아보면 좋을 것]
- 메모리 최적화: 현재 목적은 달성하셨지만, `hash_table`이라는 2차원 배열을 새로 만들지 않고 기존 `graph` 배열의 0인 공간에 직접 방문 일수(기존 값 + 1)를 누적해 나간다면 공간 복잡도를 줄일 수 있습니다.
- 네이밍 컨벤션: 4방향 이동 변수를 `n_n`, `n_m` 보다는 주로 쓰이는 `nx`, `ny` (좌표) 또는 `nr`, `nc` (row, column) 패턴으로 작성하면 다른 사람의 코드를 읽거나 내 코드를 보여줄 때 가독성이 향상될 수 있습니다.
"""