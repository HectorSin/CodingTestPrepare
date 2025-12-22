# BFS 예제

from collections import deque

def BFS(graph, start, visited):
    # 작업공간 생성 큐
    queue = deque([start])

    visited[start] = True

    while queue:
        work = queue.popleft()
        print(work, end=" ")

        for i in graph[work]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2,3,8],
    [1,7,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

BFS(graph, 1, visited)
# 출력 결과: 1 2 3 8 7 4 5 6