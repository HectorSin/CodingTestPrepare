A, B = map(int,input().split())
C, D = map(int,input().split())

num_list = [A,B,D,C]
max_num = 0
turn_time = 0

for i in range(4):
    past_num = max_num
    max_num = max(max_num, (num_list[(4-i)%4]/num_list[(7-i)%4]) + (num_list[(5-i)%4]/num_list[(6-i)%4]))
    if max_num > past_num:
        turn_time = i

print(turn_time)