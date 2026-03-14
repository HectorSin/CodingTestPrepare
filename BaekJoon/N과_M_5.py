"""
오름차순인데 두번째 숫자는 첫번째 숫자보다 작을 수 있음

이것도 같은 방식의 DFS 방식으로 접근
"""


N,M = map(int,input().split())

num_list = list(map(int,input().split()))

num_list.sort()

def DFS(depth):
    """
    """
    global visited

    if depth == M:
        answer_list = []
        for c in current_list:
            answer_list.append(num_list[c])
        print(*answer_list)
        return
    
    for i in range(N):
        if visited[i] == 1:
            continue
        else:
            visited[i] = 1
            current_list.append(i)
            DFS(depth+1)
            visited[i] = 0
            current_list.pop()

visited = [0] * N
current_list = []

DFS(0)