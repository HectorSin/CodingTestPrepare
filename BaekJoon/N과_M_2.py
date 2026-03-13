"""
1. 1~N까지 수열 M개 찾기
2. 조합들 오름차순 정렬
"""


import sys
input = sys.stdin.readline

N, M = map(int,input().split())

def DFS(depth, start):
    """
    M개의 숫자를 찾을때까지 탐색하는 함수
    """
    global M
    
    if depth == M:
        print(*arr)
        return
    
    for i in range(start,N+1):
        arr[depth] = i
        DFS(depth+1, i+1)

arr = [0] * M
DFS(0,1)
    