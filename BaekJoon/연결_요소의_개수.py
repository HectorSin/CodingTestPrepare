# 3s, 512mb 시간적 메모리적 여유 있어보임

# import sys
# input = sys.stdin.readline

# N, M = map(int,input().split())

# connection_list = [[] for _ in range(N+1)]

# for _ in range(M):
#     index, target = map(int,input().split())
#     connection_list[index].append(target)

# visited_list = []
# counter = 0

# def DFS(number):
#     global counter
#     if number in visited_list: # 방문한적 있으면 패스
#         return
    
#     counter += 1
    
#     if connection_list[number]: # 연결있다면 진행
#         check_list = connection_list[number]
#         stack = []
#         for check in check_list:
#             if check in visited_list:
#                 continue
#             else:
#                 stack.append(check)
        
#         while stack:
#             check_item = stack.pop()

#             if check_item in visited_list:
#                 continue

#             visited_list.append(check_item) # 방문처리

#             if connection_list[check_item]:
#                 for check in connection_list[check_item]:
#                     stack.append(check)
            
#     else: # 연결 없으면 끝, 1개만 존재하는 케이스
#         visited_list.append(number)
#         return



# for i in range(1,N+1):
#     DFS(i)

# print(counter)

# 테스트 케이스 통과 -> 제출 실패

"""
=== 백준 11724번 코드 리뷰 ===

[문제 이해]
- 방향 없는 그래프(Undirected Graph)가 주어지고, 연결 요소(Connected Component)의 개수를 구하는 문제입니다.
- 모든 노드를 탐색하면서, 방문하지 않은 노드가 나올 때마다 새로운 연결 요소로 카운트하고 연결된 모든 노드를 방문 처리해야 합니다.

[현재 접근 방식]
- 인접 리스트(`connection_list`)를 사용하여 그래프를 구현했습니다.
- 반복문(`1~N`)을 돌며 방문하지 않은 노드에 대해 `DFS` 함수를 호출하여 카운트를 증가시킵니다.
- `DFS` 함수 내부에서 스택을 이용한 반복적(Iterative) 탐색을 수행하고 있습니다.

[분석 결과]
- **논리적 오류 (Critical)**: 문제에서 그래프는 **방향이 없다**고 했습니다. 하지만 현재 코드는 `index, target`을 입력받을 때 `connection_list[index].append(target)`만 수행하여 **단방향(Directed)** 연결만 처리하고 있습니다. 
  - 예: 입력이 `2 1`로 들어오면 2에서 1로는 갈 수 있지만 1에서 2로는 못 가는 것으로 처리되어, 탐색 순서에 따라 연결 요소 개수가 다르게 나올 수 있습니다.
- **시간 복잡도**: `visited_list`를 리스트(`[]`)로 선언하고 `in` 연산자로 방문 여부를 확인하고 있습니다. 리스트의 `in` 연산은 O(K) 시간이 걸리므로, 전체 탐색 과정에서 비효율적입니다(전체 O(N*V) 가능).
- **예상 결과**: 그래프 방향성 처리 미흡으로 인해 '틀렸습니다' 혹은 특정 케이스 오답 예상.

[힌트]
💡 **방향 없는 그래프** 처리를 잊지 마세요.
- 간선 입력 시 양쪽 노드 모두에 서로를 추가해줘야 합니다. (`u` -> `v` 그리고 `v` -> `u`)

💡 **방문 체크 최적화**
- `visited_list`를 리스트 대신 **Boolean 배열**(`[False] * (N+1)`)이나 **집합(Set)**으로 변경해보세요. 방문 확인을 O(1)에 할 수 있어 훨씬 효율적입니다.

[더 알아보면 좋을 것]
- 재귀(Recursion) 방식의 DFS와 스택(Stack) 방식의 DFS 차이점
- BFS(너비 우선 탐색)로도 이 문제를 해결할 수 있습니다.
"""

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

connection_list = [[] for _ in range(N+1)]

for _ in range(M):
    index, target = map(int,input().split())
    connection_list[index].append(target)
    connection_list[target].append(index) # 방향 없는 그래프의 경우 이렇게 두가지 케이스 추가 필요

visited_list = [False] * (N+1)

counter = 0

def DFS(number):
    global counter
    if visited_list[number]: return
    visited_list[number] = True # 방문처리
    
    counter += 1
    
    if connection_list[number]: # 연결있다면 진행
        check_list = connection_list[number]
        stack = []
        for check in check_list:
            if visited_list[check]: continue
            else:
                stack.append(check)
        
        while stack:
            check_item = stack.pop()

            if visited_list[check_item]: continue

            visited_list[check_item] = True # 방문처리

            if connection_list[check_item]:
                for check in connection_list[check_item]:
                    stack.append(check)

for i in range(1,N+1):
    DFS(i)

print(counter)

# 제출 성공