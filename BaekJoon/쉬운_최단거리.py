# https://www.acmicpc.net/problem/14940
#
# [문제 분석]
# 이 문제는 격자판의 모든 지점에서 목표 지점(2)까지의 최단 거리를 구하는 문제입니다.
# - 목표 지점(2)에서 시작하여 BFS(너비 우선 탐색)를 수행해야 합니다.
# - 가로, 세로로만 이동 가능합니다.
# - 원래 갈 수 없는 땅(0)은 0으로 출력합니다.
# - 원래 갈 수 있는 땅(1)인데 도달할 수 없는 경우 -1을 출력해야 합니다.
#
# [코드 분석 및 피드백]
# 1. (중요) BFS 함수가 재귀적으로 호출되고 있습니다. 이는 DFS(깊이 우선 탐색) 방식이며,
#    최단 거리를 보장하지 못하고 RecursionError가 발생할 수 있습니다.
#    -> deque를 이용한 반복문 기반의 BFS로 변경해야 합니다.
# 2. (중요) visited 배열 초기화 방식 `[[0] * n] * m`은 얕은 복사(shallow copy) 문제를 일으킵니다.
#    한 행을 수정하면 모든 행이 같이 수정되는 오류가 있습니다.
#    -> `visited = [[-1] * m for _ in range(n)]` 형태로 수정하고, 방문하지 않은 곳을 -1로 초기화하는 것이 좋습니다.
# 3. 입력 변수 n(행), m(열)에 대해 visited 배열의 차원이 반대로 설정되어 있습니다. (m행 n열로 생성됨)
# 4. 시작점이 (0, 0)으로 고정되어 있습니다. 입력된 그래프에서 '2'의 위치를 찾아 그곳에서 시작해야 합니다.
# 5. 좌표 범위 체크에서 n(행)과 m(열)의 경계 조건이 섞여 있습니다.


n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

dirx = [1,-1,0,0]
diry = [0,0,1,-1]

visited = [[0] * n] * m
# 피드백: 위 초기화는 [0, 0, ...] 리스트를 m번 참조하게 만듭니다.
# 또한 n은 행의 개수, m은 열의 개수이므로 `[[0] * m for _ in range(n)]`이 되어야 합니다.
# 문제 요구사항에 따라 방문하지 못한 곳은 -1, 벽은 0으로 처리해야 하므로,
# 초기값을 -1로 채우고, 그래프가 0인 곳은 0으로 전처리하는 방식을 추천합니다.

def bfs(graph,s_x, s_y):
    # 피드백: 재귀 호출을 사용하면 DFS가 됩니다. 
    # from collections import deque를 사용해서 큐를 만들고,
    # while q: 루프를 사용하는 정석적인 BFS 구조로 변경해주세요.
    # 거리 저장은 visited 배열에 (이전 위치 값 + 1)을 저장하는 방식을 사용하세요.
    for dir in range(4):
        next_x = s_x + dirx[dir]
        next_y = s_y + diry[dir]

        if next_x < 0 or next_x >= m or next_y < 0 or next_y >= m:
            pass

        if graph[next_x][next_y] == 0:
            pass

        if visited[next_x][next_y] == 0:
            visited[next_x][next_y] += 1
            bfs(graph, next_x, next_y)

# 피드백: 시작점이 무조건 (0,0)이 아닙니다.
# 그래프 전체를 순회(for문 2개)하여 값이 2인 지점(target_x, target_y)을 찾고,
# bfs(graph, target_x, target_y)를 호출해야 합니다.
# bfs 호출 전, visited[target_x][target_y] = 0 으로 시작점을 설정하세요.
bfs(graph, 0, 0)

for a in visited:
    for b in a:
        print(b, sep=' ')
# 피드백: 각 행의 원소를 공백으로 구분해서 출력해야 합니다.
# print(*a) 를 사용하면 더 간단하게 한 줄을 출력할 수 있습니다.
    print('')