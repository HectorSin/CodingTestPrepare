"""
N과 M이 주어졌을때 조건을 만족하는 수열 찾기

DFS방식을 활용해서 재귀함수 활용
"""

N, M = map(int,input().split())

def DFS(depth,start_num):
    """
    depth 깊이
    start_num 시작 숫자
    """
    if depth == M:
        print(*current)
        return
    
    for i in range(start_num, N+1):
        current[depth] = i
        DFS(depth+1,i)

current = [0] * M

DFS(0,1)