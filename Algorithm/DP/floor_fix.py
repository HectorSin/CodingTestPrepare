"""
바닥 공사
"""
# 1s 128mb

N = int(input()) # 1~1000

dp_table = [0] * (N+1)

dp_table[1] = 1
dp_table[2] = 3

for i in range(3,N+1):
    dp_table[i] = dp_table[i-1] + dp_table[i-2]*2

print(dp_table[N])