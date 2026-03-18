"""
1부터 시작하는 트리에서 각 노드의 부모 노드 찾기
2~100,000

BFS 방식 사용
"""

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())

connection = [[] for _ in range(N+1)]


for _ in range(N-1):
    n1, n2 = map(int,input().split())
    
    connection[n1].append(n2)
    connection[n2].append(n1)
    
parent_con = [0] * (N+1)
visited = [0] * (N+1)

def BFS():
    global parent_con
    global visited
    
    q = deque()
    q.append(1)
    
    parent_con[1] = 1
    parent = 1
    
    while q:
        current = q.popleft()
        
        child_list = connection[current]
           
        for child in child_list:
            if visited[child] == 0:
                visited[child] = 1
                parent_con[child] = current
                q.append(child)
                
BFS()

for i in range(2,N+1):
    print(parent_con[i])