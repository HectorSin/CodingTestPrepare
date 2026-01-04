"""
개미 전사
"""
# 1s 128mb

N = int(input())
food_list = list(map(int,input().split()))

dp_table = [0] * 101
dp_table[1] = food_list[0]
if N>=2:
    dp_table[2] = max(dp_table[1], food_list[1])

if N>=3:
    for i in range(3,N+1):
        dp_table[i] = max(dp_table[i-1], dp_table[i-2] + food_list[i-1])

print(dp_table[N])