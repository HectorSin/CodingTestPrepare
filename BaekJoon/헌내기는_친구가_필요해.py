# 1s, 1024 mb

# O 빈공간, X 벽, I 도연, P 사람

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int,input().split())

map_list = []

for i in range(N):
    map_text = input().rstrip()
    temp_list = []
    for j, m in enumerate(map_text):
        if m == "I":
            do_place = [i,j]
        temp_list.append(m)
    map_list.append(temp_list)

graph = [[0 for _ in range(M)] for _ in range(N)] # 방문 체크
dx = [1,0,-1,0]
dy = [0,-1,0,1]

def BFS(s_row, s_col):
    counter = 0 # 사람 만났는지 체크
    
    queue = deque()
    queue.append((s_row,s_col))
    
    graph[s_row][s_col] = 1 # 방문 처리

    while queue:
        check_x, check_y = queue.popleft()

        for i in range(4):
            next_x = check_x + dx[i]
            next_y = check_y + dy[i]

            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M: # 범위를 벗어나는 경우 pass
                continue

            if map_list[next_x][next_y] == "X":
                continue

            if graph[next_x][next_y] == 1: # 이미 방문한 경우 pass
                continue

            if map_list[next_x][next_y] == "P":
                counter += 1
            
            graph[next_x][next_y] = 1 # 방문 처리
            queue.append((next_x,next_y))

    return counter


count = BFS(do_place[0], do_place[1])

if count == 0:
    print("TT")
else:
    print(count)

"""
=== 백준 21736번 코드 리뷰 ===

[문제 이해]
- N x M 크기의 캠퍼스에서 도연(I)이가 만날 수 있는 사람(P)의 수를 구하는 문제입니다.
- 벽(X)은 통과할 수 없으며, 아무도 만나지 못하면 "TT"를 출력해야 합니다.

[현재 접근 방식]
- BFS(너비 우선 탐색)를 사용하여 도연이의 위치에서 시작해 상하좌우로 탐색합니다.
- `map_list` 자체를 방문 배열로 사용하여 방문한 곳을 1로 변경하고 있습니다.

[분석 결과]
- 시간 복잡도: O(N x M) - 모든 좌표를 최대 한 번씩 방문하므로 효율적입니다.
- 공간 복잡도: O(N x M) - 지도 및 큐 사용 적절합니다.
- 예상 결과: 정답 (Pass)

[더 알아보면 좋을 것]
1. BFS(너비 우선 탐색) vs DFS(깊이 우선 탐색)
   - BFS (Breadth-First Search):
     - 방식: 시작 노드에서 가까운 노드부터 차례대로 탐색 (큐 사용)
     - 장점: 최단 거리(또는 최소 단계)를 구해야 할 때 유리
     - 단점: 큐에 많은 노드를 저장해야 하므로 메모리 사용량이 클 수 있음
   - DFS (Depth-First Search):
     - 방식: 한 방향으로 갈 수 있을 때까지 깊게 들어갔다가 되돌아옴 (스택 또는 재귀 사용)
     - 장점: 메모리 사용이 비교적 적을 수 있음 (경로상의 노드만 저장)
     - 단점: 최단 경로 보장 안 됨, 해가 없는 깊은 경로에 빠질 수 있음
   - *이 문제(21736)는 모든 연결된 구간을 탐색하는 것이므로 BFS/DFS 둘 다 가능합니다.*

2. 불필요한 메모리 할당 줄이기
   - 현재 코드에서는 `map_list`와 별도로 `graph`라는 2차원 배열을 만들고 있지만, 
     실제로는 `map_list`의 값을 직접 변경하거나 `graph`를 제대로 활용하지 않는 부분이 있었습니다.
   - 최적화 방법:
     - 방법 1: `visited` 배열을 `bool` 타입 등으로 별도 생성하여 방문 여부만 관리 (원본 지도 보존)
     - 방법 2: 입력받은 `map_list`에 방문 표시를 직접 기록 (추가 메모리 0, 원본 지도 변형)
       -> 예: 방문한 곳을 'X'나 'V'로 변경
   - 이렇게 하면 불필요하게 `graph` 배열(NxM 크기)을 선언하고 사용하지 않는 낭비를 막을 수 있습니다.
"""