# 2s, 128mb
import sys
input = sys.stdin.readline

K,N = map(int,input().split())
line_list = []

for _ in range(K):
    line_list.append(int(input()))

max_line = max(line_list) # output의 최대치

result = 0
start = 1
end = max_line

while start <= end:
    mid = (start + end) // 2
    count = 0
    for line in line_list:
        count += line // mid
    
    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)