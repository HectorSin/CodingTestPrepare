# 정사각형
# 1는 집 0는 빈 곳

# 연결된 집을 찾는 문제

# 집을 찾는 함수를 모든 위치에 돌리기

# 방문했는지 체크
# 방문 안했는데 집이라면 BFS 방식 사용하여 인접한 모든 집 방문 & 라벨링
# 모든 작업 끝난후 방문 리스트의 각 집 개수 count

# from collections import Counter, deque
# import sys

# input = sys.stdin.readline

# N = int(input())

# visit_graph = [[0] * N for _ in range(N)]
# map_graph = []

# dx = [1,0,-1,0]
# dy = [0,-1,0,1]

# current_num = 0

# for _ in range(N):
#     each_graph = input().rstrip()
#     map_graph.append(list(each_graph)) # str로 저장

# def BFS(x,y):
#     global current_num

#     # 방문 여부 집 여부 체크
#     if visit_graph[x][y] != 0 or map_graph[x][y] != '1':
#         return
    
#     q = deque()
#     q.append([x,y])

#     current_num += 1

#     while q:
#         current_loc = q.popleft()

#         for i in range(4):
#             next_x = current_loc[0] + dx[i]
#             next_y = current_loc[1] + dy[i]

#             if 0 <= next_x < N and 0 <= next_y < N and visit_graph[next_x][next_y] == 0 and map_graph[next_x][next_y] == '1':
#                 visit_graph[next_x][next_y] = current_num
#                 q.append([next_x,next_y])

# for i in range(N):
#     for j in range(N):
#         BFS(i,j)

# counts = []
# for i in visit_graph:
#     for j in i:
#         if j != 0:
#             counts.append(j)

# counts_dict = Counter(counts)

# houses = counts_dict.keys()

# print(len(houses)) # 집 개수 출력

# house_list = []
# for i in houses:
#     house_list.append(counts_dict[i])

# house_list.sort()

# for i in house_list:
#     print(i)

"""
=== 백준 2667번 코드 리뷰 ===

[문제 이해]
- NxN 정사각형 지도에서 연결된 집들의 단지를 찾는 문제
- 각 단지에 속한 집의 수를 오름차순으로 출력

[설계 프로세스 평가]
- 주석 작성 여부: O (간단한 주석 있음)
- 문제 분석 단계: 보완 필요 (기본 아이디어만 있음)
- 자료구조 선택 근거: 불명확 (왜 BFS를 선택했는지 명시 안됨)
- 알고리즘 설계: 추상적 (단계별 구체적 설명 부족)
- 설계-구현 일치도: 부분 불일치 (구현에 버그 있음)

[현재 접근 방식]
- BFS를 사용하여 연결된 집들을 탐색하고 라벨링
- visit_graph로 방문 여부 및 단지 번호 관리
- Counter를 사용하여 각 단지의 집 개수 계산

[분석 결과]
- 시간 복잡도: O(N^2) - 모든 칸을 한 번씩 방문
- 공간 복잡도: O(N^2) - visit_graph, map_graph 사용
- 예상 결과: ⚠️ 틀림 (로직 오류 있음)

[힌트]
💡 좋은 접근이지만 작은 버그가 있습니다!
- BFS 시작점 처리를 다시 확인해보세요
- 현재 코드에서 (x, y) 위치가 방문 처리되지 않는 경우가 있습니다
- 큐에 넣을 때와 방문 처리 시점을 생각해보세요

[설계 개선 제안]
다음번에는 코드 작성 전 이런 구조로 주석을 작성해보세요:

[문제 분석]
- NxN 지도에서 상하좌우로 연결된 집(1)들의 그룹 찾기
- 각 그룹의 크기를 오름차순 출력
- N 최대 25 -> O(N^2) 가능

[자료구조 선택]
- 그래프 탐색 문제 -> BFS 또는 DFS
- BFS 선택 이유: 레벨별 탐색이 직관적, 큐 사용
- 방문 체크: 2차원 배열 (방문 여부 + 단지 번호 동시 저장)

[알고리즘]
1. 모든 칸 순회하며 미방문 집(1) 발견 시 BFS 시작
2. BFS: 시작점 방문 처리 -> 큐에 추가 -> 4방향 탐색
3. 각 단지별 집 개수 카운트
4. 결과 정렬 후 출력

[주의사항]
- 시작점도 방문 처리 필수!
- 큐에 넣을 때 즉시 방문 처리 (중복 방지)

[복잡도]
- 시간: O(N^2)
- 공간: O(N^2)

[구체적인 버그]
35번째 줄에서 BFS 함수 시작 시 조건 체크만 하고 return하는데,
실제로 BFS를 시작할 때 **시작점 (x, y) 자체를 방문 처리하지 않았습니다**.

현재 로직:
- 39번 줄: q.append([x,y]) - 큐에 추가
- 44번 줄: q.popleft() - 꺼내기
- 하지만 visit_graph[x][y]는 설정 안 함!
- 50-51번 줄: 인접 칸만 방문 처리

결과: 시작점이 카운트되지 않아 각 단지의 집 개수가 1씩 부족합니다.

💡 해결 방법을 생각해보세요:
- 시작점을 언제 방문 처리해야 할까요?
- 큐에 넣기 전? 후? 꺼낸 후?

[더 알아보면 좋을 것]
- BFS vs DFS 선택 기준
- 방문 처리 타이밍 (큐 삽입 시 vs 꺼낼 때)
- 그래프 탐색 문제의 일반적인 패턴
- 문제 해결 전 상세한 설계 주석 작성의 중요성

[격려]
전체적인 접근 방식은 정확합니다! 작은 실수만 고치면 바로 통과할 수 있어요.
이런 경험이 쌓이면 비슷한 실수를 사전에 방지할 수 있습니다. 화이팅! 💪
"""

from collections import Counter, deque
import sys

input = sys.stdin.readline

N = int(input())

visit_graph = [[0] * N for _ in range(N)]
map_graph = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]

current_num = 0

for _ in range(N):
    each_graph = input().rstrip()
    map_graph.append(list(each_graph)) # str로 저장

def BFS(x,y):
    global current_num

    # 방문 여부 집 여부 체크
    if visit_graph[x][y] != 0 or map_graph[x][y] != '1':
        return
    
    q = deque()
    q.append([x,y])

    current_num += 1
    visit_graph[x][y] = current_num

    while q:
        current_loc = q.popleft()

        for i in range(4):
            next_x = current_loc[0] + dx[i]
            next_y = current_loc[1] + dy[i]

            if 0 <= next_x < N and 0 <= next_y < N and visit_graph[next_x][next_y] == 0 and map_graph[next_x][next_y] == '1':
                visit_graph[next_x][next_y] = current_num
                q.append([next_x,next_y])

for i in range(N):
    for j in range(N):
        BFS(i,j)

counts = []
for i in visit_graph:
    for j in i:
        if j != 0:
            counts.append(j)

counts_dict = Counter(counts)

houses = counts_dict.keys()

print(len(houses)) # 집 개수 출력

house_list = []
for i in houses:
    house_list.append(counts_dict[i])

house_list.sort()

for i in house_list:
    print(i)