# 10*10의 보드판이라고 했지만 1~100 번까지 일렬로 나열된 보드칸이라고 생각해도 됨
# 사다리 [+], 뱀 [-] 조건이 있음
# 결국 최소 주사위 개수를 구하는 것이므로 while문으로 도착할때까지 진행하고
# 해쉬테이블에서 최소 주사위 회수를 저장하는 방식으로 진행

# BFS 방식으로 진행 [함수 만들어서]
# 1. q에서 현재 위치 꺼냄
# 2. 다음 위치 6가지를 전부 진행
# 3. 우선 100번째 달성하면 return

# import sys
# from collections import defaultdict, deque

# input = sys.stdin.readline

# N, M = map(int,input().split())

# ladder_dic = defaultdict()
# snake_dic = defaultdict()

# for _ in range(N):
#     x,y = map(int,input().split())
    
#     ladder_dic[x] = y
    
# for _ in range(M):
#     u,v = map(int,input().split())
    
#     snake_dic[u] = v
    

# def find_dice():
#     """
#     100번까지 가는 주사위 수 찾는 함수
#     """
#     global ladder_dic, snake_dic
    
#     hash_table = [0] * 101
#     q = deque()
#     q.append(0)
    
#     while q:
#         current = q.popleft()
        
#         for i in range(1,7):
#             next_place = current + i
            
#             if next_place in ladder_dic:
#                 next_place = ladder_dic[next_place]
#             elif next_place in snake_dic:
#                 next_place = snake_dic[next_place]
            
#             if hash_table[next_place] == 0:
#                 hash_table[next_place] = hash_table[current] + 1
#                 q.append(next_place)
            
#             if next_place == 100:
#                 # print(hash_table)
#                 return hash_table[100]
    

# print(find_dice())

"""
=== 백준 16928번 코드 리뷰 ===

[문제 이해]
- 이 문제는 1번 칸에서 100번 칸까지 주사위를 굴려 이동할 때, 뱀과 사다리를 고려하여 최소 주사위 굴림 횟수를 구하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O
- 문제 분석 단계: 보완 필요 (보드의 시작 조건과 범위를 조금 더 명확히 할 수 있습니다)
- 자료구조 선택 근거: 명확함 (최단 거리 탐색을 위한 큐와 해시테이블 사용)
- 알고리즘 설계: 구체적
- 설계-구현 일치도: 부분 불일치 (도달 시나리오는 있으나, 100을 넘어가는 경우에 대한 처리가 누락되었습니다)

[현재 접근 방식]
- BFS를 활용하여 모든 가능한 이동(1~6)을 탐색하며 해시테이블(`hash_table`)에 최소 이동 횟수를 기록하고 있습니다.

[분석 결과]
- 시간 복잡도: O(V + E) (칸의 개수 100, 각 칸별 이동 6가지)
- 예상 결과: 런타임 에러 (IndexError) 및 틀림

[힌트]
💡 탐색 과정에서 몇 가지 예외 케이스를 다시 확인해보세요.
- 주사위를 굴렸을 때 100번 칸을 넘어가는 경우(`next_place > 100`) 어떻게 될까요?
- 문제에서 시작 위치는 0 번지일까요, 1 번지일까요? 
- 출발점의 방문 처리가 `hash_table`에서 0으로 남아있어 다른 곳에서 출발점을 다시 방문하게 될 가능성은 없을까요?

[설계 개선 제안]
다음 구조로 조건을 좀 더 명확히 기록해두면 놓치는 부분을 줄일 수 있습니다:
1. 시작과 끝 위치 명확화 (예: 시작 1, 끝 100)
2. 인덱스 범위를 초과하는 경우의 예외 처리
3. 초기 상태(출발점)의 방문 확인 처리 로직

[더 알아보면 좋을 것]
- BFS 과정에서 '방문 여부 처리를 큐에 넣기 전에 하는 것'과 '큐에서 꺼낸 후 하는 것'의 차이
"""

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M = map(int,input().split())

ladder_dic = defaultdict()
snake_dic = defaultdict()

for _ in range(N):
    x,y = map(int,input().split())
    
    ladder_dic[x] = y
    
for _ in range(M):
    u,v = map(int,input().split())
    
    snake_dic[u] = v
    

def find_dice():
    """
    100번까지 가는 주사위 수 찾는 함수
    """
    global ladder_dic, snake_dic
    
    hash_table = [0] * 101

    q = deque()
    q.append(1)
    
    while q:
        current = q.popleft()
        
        for i in range(1,7):
            next_place = current + i
            
            if next_place > 100 or next_place <= 1:
                continue
            
            if next_place in ladder_dic:
                next_place = ladder_dic[next_place]
            elif next_place in snake_dic:
                next_place = snake_dic[next_place]
            
            if hash_table[next_place] == 0:
                hash_table[next_place] = hash_table[current] + 1
                q.append(next_place)
            
            if next_place == 100:
                # print(hash_table)
                return hash_table[100]
    

print(find_dice())
