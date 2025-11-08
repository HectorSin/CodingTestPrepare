N, M = map(int,input().split())

d = [[0]*M for _ in range(N)]

x,y,direction = map(int,input().split())

d[x][y] = 1

array = []
for i in range(N):
    array.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)





# N, M = map(int,input().split())
# A, B, dir = map(int,input().split()) # B 행 A 열
# # A -= 1
# # B -= 1

# map = []
# for i in range(N):
#     map.append(input().split())

# dir_list = [0,1,2,3]
# move_list = [(0,1),(1,0),(0,-1),(-1,0)]

# moved_location = []

# # 계속 진행
# while True:
#     success = False
#     # 1 단계
#     for i in range(4):
#         if success == False:
#             dir -= 1
#             if dir < 0:
#                 dir = 3
#             next_row = B + move_list[dir][0]
#             next_column = A + move_list[dir][1]

#             # 가봤던 곳 or 바다인 곳
#             if (next_row,next_column) in moved_location or map[next_row][next_column] == 1:
#                 pass
            
            
#             else:
#                 success = True
#                 moved_location.append((next_row,next_column))
#                 B = next_row
#                 A = next_column
    
#     # 3 단계
#     if success == False:
#         B -= move_list[dir][0]
#         A -= move_list[dir][1]

#     # 3 단계 실패
#     if B < 0 or A < 0 or B > M or B > N:
#         break
#     if map[B][A] == 1:
#         break

# # print(len(moved_location))
# print(moved_location)