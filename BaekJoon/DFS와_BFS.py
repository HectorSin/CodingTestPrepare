# 2s, 128MB
"""
# 문제 분석: 백준 1260 DFS와 BFS (https://www.acmicpc.net/problem/1260)
# - N개의 정점과 M개의 간선이 주어질 때, DFS와 BFS 탐색 결과를 출력해야 합니다.
# - 방문할 수 있는 정점이 여러 개인 경우 정점 번호가 작은 것을 먼저 방문해야 합니다.
# - N=1,000, M=10,000으로 시간 제한 2초는 비교적 여유롭습니다.

# 현재 접근 분석:
# - Dictionary를 이용한 인접 리스트 방식을 사용했습니다. (좋습니다!)
# - 재귀함수가 아닌 스택을 이용한 DFS 구현은 파이썬의 재귀 깊이 제한을 피할 수 있어 좋은 선택입니다.

# 힌트 (Level 1 - 버그 수정):
# - 만약 시작 정점 V가 어떤 정점과도 연결되지 않은 '고립된 정점'이라면 어떻게 될까요?
# - 현재 코드에서는 `neighbors` 변수가 정의되지 않아 에러가 발생할 수 있습니다. (NameError)
# - `neighbors`를 미리 빈 리스트로 초기화하거나, 조건문 처리를 확인해보세요.

# 힌트 (Level 2 - 최적화):
# - DFS와 BFS 함수 안에서 매번 `sorted()`를 호출하고 있습니다.
# - 그래프 입력이 끝난 직후(탐색 시작 전)에 미리 리스트를 정렬해두면 어떨까요?
# - BFS의 경우 큐에 넣을 때 방문 처리를 하는 것이 중복 방문을 줄이는 데 더 효율적일 수 있습니다.
"""

from collections import deque
import sys
input = sys.stdin.readline

N,M,V = map(int,input().split())

con_dict = {}

for _ in range(M):
    a, b = map(int,input().split())
    if a not in con_dict: # 비어 있다면 추가
        con_dict[a] = []
    if b not in con_dict:
        con_dict[b] = []
    if b not in con_dict[a]:
        con_dict[a].append(b)
    if a not in con_dict[b]:
        con_dict[b].append(a)

for c in con_dict:
    con_dict[c] = sorted(con_dict[c])

def DFS(start):
    visit_list = []
    stack = [start]

    while stack:
        current_point = stack.pop()

        if current_point in visit_list:
            continue
        
        visit_list.append(current_point)

        neighbors = []
        if current_point in con_dict:
            neighbors = con_dict[current_point][::-1]
        
        for n in neighbors:
            stack.append(n)

    return visit_list

print(*DFS(V))


def BFS(start):
    visit_list = [start]
    queue = deque([start])

    while queue:
        current_point = queue.popleft()

        neighbors = []
        if current_point in con_dict:
            neighbors = con_dict[current_point]

        for n in neighbors:
            if n not in visit_list:
                visit_list.append(n)
                queue.append(n)

    return visit_list

print(*BFS(V))