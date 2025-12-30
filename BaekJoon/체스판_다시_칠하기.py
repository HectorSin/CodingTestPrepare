# 2s 128mb
# 64~2500 O(N^2)ok


import sys
input = sys.stdin.readline

N, M = map(int,input().split())

board_list = [] # 바둑판

for _ in range(N):
    string = input().rstrip()
    board_list.append(list(string))

def color_changer(color):
    if color == "B":
        return "W"
    else:
        return "B"
    
# 8*8 리스트를 주면 최소 색칠 칸을 알려주는 함수
def min_color_change(sub_board):
    current_board = sub_board[0][0] # 현재 칸 색 B or W
    line_board = sub_board[0][0] # B or W 각 줄 첫번째 칸 색
    counter = 0 # 몇개 다시 칠해야하는지 체크 - 최소치이기에 32 보다 크면 64를 뺀 값
    for i in range(8):
        for j in range(8):
            if sub_board[i][j] != current_board:
                counter += 1
            current_board = color_changer(current_board)
        line_board = color_changer(line_board)
        current_board = line_board
    if counter > 32:
        counter = 64 - counter
    
    return counter


min_number = 64

for a in range(N-7):
    for b in range(M-7):
        current_num = min_color_change([row[b:b+8] for row in board_list[a:a+8]])
        min_number = min(min_number, current_num)

print(min_number)