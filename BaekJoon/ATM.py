# 1s, 256mb

N = int(input())

num_list = list(map(int,input().split()))

num_list.sort()

added_time = 0
final_time = 0

for num in num_list:
    added_time += num
    final_time += added_time

print(final_time)