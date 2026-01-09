import sys
from collections import deque
input = sys.stdin.readline

T = int(input()) # test case

def find_near_b(b_list, x, y):
    queue = deque()
    queue.append([x,y])

    next_x = [1,0,-1,0]
    next_y = [0,-1,0,1]

    while queue:
        work_place = queue.popleft()

        for i in range(4):
            next_spot = [work_place[0] + next_x[i], work_place[1] + next_y[i]]
            if next_spot[0] < 0 or next_spot[0] >= M or next_spot[1] < 0 or next_spot[1] >= N:
                continue

            if visit_list[next_spot[0]][next_spot[1]] == 1: # 이미 방문했다면
                continue

            if b_list[next_spot[0]][next_spot[1]] == 1: # 배추가 있는 곳이라면
                queue.append([next_spot[0], next_spot[1]]) # 큐 추가
                visit_list[next_spot[0]][next_spot[1]] = 1 # 방문처리
            else:
                continue




for _ in range(T):
    M, N, K = map(int,input().split()) # 가로, 세로, 배추개수

    board_list = [[0] * N for _ in range(M)] # 배추 위치

    visit_list = [[0] * N for _ in range(M)] # 방문 판

    for _ in range(K):
        X,Y = map(int,input().split())
        board_list[X][Y] = 1

    counter = 0

    for i in range(M):
        for j in range(N):
            if board_list[i][j] == 1 and visit_list[i][j] == 0:
                counter += 1
                find_near_b(board_list, i, j)
    
    print(counter)

