"""
부품 찾기
"""
# 1s, 128mb

N = int(input()) # 1,000,000
source_list = list(map(int,input()))
M = int(input()) # 100,000
find_list = list(map(int,input())) 

source_hash = [0] * 1000001
for i in source_list:
    source_hash[i] += 1

for j in find_list:
    if source_hash[j] >= 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")