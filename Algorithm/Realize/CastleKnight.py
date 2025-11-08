# 왕실의 나이트

# 8 X 8 크기의 체스판의 랜덤한 위치에 나이트가 배치
# 해당 나이트가 이동할 수 있는 모든 경우의 수 찾기 문제

location = input()

row = int(location[1])

column_list = ['a','b','c','d','e','f','g','h']
column = column_list.index(location[0])

# count = 8

# if row < 3 or row > 6:
#     count -= 4
#     if column < 3 or column > 6:
#         count -= 2
# else:
#     if column < 3 or column  > 6:
#         count -= 4

# print(count)

move_list = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]

count = 0

for move in move_list:
    move_row = row + move[0]
    move_column = row + move[1]
    if move_row <= 8 and move_row >= 1 and move_column <= 8 and move_column >= 1:
        count += 1

print(count)