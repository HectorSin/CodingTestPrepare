# https://www.acmicpc.net/problem/1389

# 케빈베이커 수 가장 작은 사람 구하는 프로그램 [여러명인경우 숫자가 가장 작은 사람]

# 관계 중복 가능 [중복 체크 필요]

# 가장 깊은 단계가 아닌 가장 짧은 길이를 찾는 방식이기에 BFS 사용

# 중복이 될 수 있기에 set 사용 & dictionary 사용

# from collections import defaultdict

# N, M = map(int,input().split()) # N 2~100 M 1~5000

# connection_dict = defaultdict(set)

# for _ in range(M):
#     A, B = map(int,input().split())
#     connection_dict[A].add(B)
#     connection_dict[B].add(A)

# def find_cavin(number):
#     """
#     number의 케빈베이커 수 return
#     """
#     global connection_dict

#     hash_list = [0] * (N+1)

#     stack = []
#     stack.append([number])

#     connection_num = 0

#     while stack:
#         check_list = stack.pop()

#         next_stack = []

#         connection_num += 1
#         for c in check_list:
#             if hash_list[c] == 0 and c != number:
#                 hash_list[c] = connection_num
#             else:
#                 for next in connection_dict[c]:
#                     if hash_list[next] == 0 and next != number:
#                         next_stack.append(next)
        
#         stack.append(next_stack)

#     result = 0

#     for num in hash_list:
#         result += num

#     return result

# min_cavin = 101
# min_num = 0

# for i in range(1,N+1):
#     cavin = find_cavin(i)
#     if cavin < min_cavin:
#         min_num = i
#         min_cavin = cavin

# print(min_num)



# 현재 상태에서 30분 시간 초과
# 우선 set사용이나, 어떤 알고리즘 사용인지 초반에 정확하게 정하고 주석으로 그림을 그린 후에 들어가자
# 구현하면서 들어가다보니 시간도 더 걸리고 중간에 한번 길을 잃으면 끝까지 잃어버린다

"""
=== 백준 1389번 코드 리뷰 ===

[문제 이해]
- 유저 간의 단계 수(케빈 베이컨 수)가 가장 작은 사람을 찾는 문제
- 친구 관계는 양방향 그래프

[설계 프로세스 평가]
- 주석 작성 여부: O (시도하였으나 중단됨)
- 설계-구현 일치도: 낮음
- 스스로 "길을 잃었다"고 판단하신 점이 매우 중요합니다. 코딩 전에 손으로 로직을 구체화하는 단계가 필요해 보입니다.

[현재 접근 방식]
- 각 유저별로 BFS를 수행하여 거리를 계산하려 함
- Stack을 이용한 레벨 단위 탐색 시도

[분석 결과]
- ⚠️ 치명적인 로직 오류:
  `if hash_list[c] == 0` (방문 안 함) 일 때 방문 처리를 하고,
  `else` (이미 방문함) 일 때만 이웃을 탐색하고 있습니다.
  → 처음 방문한 노드는 절대 이웃을 큐에 넣지 못하고 탐색이 종료됩니다.
- 예상 결과: 거의 모든 결과가 1 또는 0으로 나올 것으로 예상 (탐색 불가)

[힌트]
💡 BFS의 핵심 흐름을 다시 잡아보세요
1. 큐에서 노드 꺼내기
2. (선택) 방문 여부 확인 (큐에 넣을 때 체크했다면 생략 가능)
3. 연결된 모든 이웃 확인
4. 이웃이 방문 안 했다면? -> 방문 처리(거리 기록) + 큐에 넣기

[설계 개선 제안]
지금 작성하신 코드 구조도 수정 가능하지만, 
N이 100으로 작으니 '플로이드-워셜' 알고리즘을 사용하면 3중 반복문으로 매우 간단히 모든 거리를 구할 수 있습니다.

[더 알아보면 좋을 것]
- BFS 표준 구현 (Queue 사용 및 방문 처리 시점)
- 플로이드-워셜 알고리즘 (모든 쌍 최단 경로)
"""


"""
[모범 설계 예시] - 코딩 전 이 정도 설계를 주석으로 작성해보세요

1. 문제 분석
- 목표: 모든 유저와의 케빈 베이컨 수(단계 합)가 가장 작은 사람 구하기
- 조건: 유저 수 N(2~100), 친구 관계 M(1~5,000), 양방향 친구 관계
- 출력: 단계 합이 가장 작은 사람의 번호 (여러 명이면 작은 번호)

2. 자료구조 선택
- 친구 관계 저장: 
  - N이 작고 M이 비교적 많음 -> 인접 리스트 (Dictionary of Sets 또는 Array of Lists)
  - 이유: 메모리 효율적이고, 연결된 친구만 바로 순회 가능
- 탐색 도구:
  - BFS (너비 우선 탐색) -> 최단 거리를 구해야 하므로 적합
  - Queue (deque 사용) -> BFS 구현에 필수
  - Visited Array -> 방문 여부 및 거리 저장 (distance 배열)

3. 알고리즘 설계 (BFS 방식)
- 모든 유저(1~N)에 대해 각각 BFS 수행 (Start Node: i)
  a. distance 배열을 -1로 초기화 (방문 안함 표시), start는 0
  b. Queue에 start 넣기
  c. Queue가 빌 때까지 반복:
     - 현재 노드 current를 popleft
     - current의 친구들을 순회:
       - 아직 방문 안 했다면(distance == -1):
         - distance[next] = distance[current] + 1
         - Queue에 next 추가
  d. distance 배열의 합을 구함 (방문 못한 곳 제외, 여기선 모두 연결됨 가정)
  e. 최소 합을 갱신하며 최소 유저 번호 기록

4. 복잡도 예측
- 시간 복잡도: 
  - BFS 1회: O(N + M) (모든 노드와 간선 확인)
  - N명의 유저에 대해 반복: O(N * (N + M))
  - N=100, M=5000 -> 100 * 5100 ≈ 500,000 연산 (매우 여유로움)
"""

import sys
from collections import defaultdict, deque

N, M = map(int,input().split()) # N 2~100 M 1~5000

connection_dict = defaultdict(set)

for _ in range(M):
    A, B = map(int,input().split())
    connection_dict[A].add(B)
    connection_dict[B].add(A)

def find_cavin(number):
    """
    number의 케빈베이커 수 return
    설계대로 BFS 방식 사용
    """
    global connection_dict

    distance_list = [-1] * (N+1)

    queue = deque()
    
    distance_list[0] = 0
    distance_list[number] = 0

    queue.append(number)

    while queue:
        current = queue.popleft()

        for friend in connection_dict[current]:
            if distance_list[friend] == -1:
                distance_list[friend] = distance_list[current] + 1
                queue.append(friend)

    return sum(distance_list)

min_cavin = sys.maxsize
min_num = 0

for i in range(1,N+1):
    cavin = find_cavin(i)
    if cavin < min_cavin:
        min_num = i
        min_cavin = cavin

print(min_num)