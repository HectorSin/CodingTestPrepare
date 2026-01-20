# # 1s 1024mb 메모리 여유가 큰 문제

# import sys
# input = sys.stdin.readline

# N, M, B = map(int,input().split()) # 세로, 가로, 보유하고 있는 블록

# hash_table = [0] * 257

# for _ in range(N):
#     for i in list(map(int,input().split())):
#         hash_table[i] += 1

# # 해쉬테이블 뒤의 빈 값 제거
# for _ in range(257):
#     check_num = hash_table.pop()
#     if check_num != 0:
#         hash_table.append(check_num)
#         break

# min_time = 9999999
# max_height = 0

# for i in range(len(hash_table)):
#     counter = 0
#     available_block = B
#     need_block = 0
#     for j in range(len(hash_table)):
#         if j < i:
#             put_block = hash_table[j] * (i - j) # 설치해야하는 블럭 개수
#             counter += put_block
#             need_block += put_block
#         elif i == j:
#             pass
#         elif j > i:
#             dig_block = 2 * hash_table[j] * (j - i) # 파는 블럭 개수
#             counter += dig_block
#             available_block += dig_block

#     if counter <= min_time and available_block >= need_block:
#         max_height = i
#         min_time = counter

# print(min_time, max_height)



# 1s 1024mb 메모리 여유가 큰 문제

import sys
input = sys.stdin.readline

N, M, B = map(int,input().split()) # 세로, 가로, 보유하고 있는 블록

hash_table = [0] * 257

for _ in range(N):
    for i in list(map(int,input().split())):
        hash_table[i] += 1

# 해쉬테이블 뒤의 빈 값 제거
for _ in range(257):
    check_num = hash_table.pop()
    if check_num != 0:
        hash_table.append(check_num)
        break

min_time = sys.maxsize
max_height = 0

for i in range(len(hash_table)):
    time_counter = 0
    available_block = B
    need_block = 0
    for j in range(len(hash_table)):
        if j < i:
            put_block = hash_table[j] * (i - j) # 설치해야하는 블럭 개수
            time_counter += put_block
            need_block += put_block
        elif i == j:
            pass
        elif j > i:
            dig_block = hash_table[j] * (j - i) # 파는 블럭 개수
            time_counter += dig_block * 2
            available_block += dig_block

    if time_counter <= min_time and available_block >= need_block:
        max_height = i
        min_time = time_counter

print(min_time, max_height)

"""
=== 백준 18111번 재검토 결과 ===

[수정 사항 확인]
- `dig_block` (개수)과 `time_counter` (시간)를 정확히 분리하셨습니다.
- 인벤토리에는 블록 개수만 더하고, 시간에는 2배를 곱해 더하는 로직이 완벽합니다.
- 변수명도 명확해져서 가독성이 좋아졌습니다.

[추가 점검 포인트]
- **초기값 설정 주의**: `min_time = 9999999` (약 1천만)
  - 최악의 경우: 500x500 땅을 전부 256번 깎아야 한다면?
  - 250,000칸 * 256층 * 2초 = 약 1억 2천 8백만(128,000,000) 시간이 소요될 수 있습니다.
  - 현재 초기값(9,999,999)보다 커질 수 있어, 최소값을 갱신하지 못하고 틀린 답을 내놓을 위험이 있습니다.
  
[피드백]
💡 `min_time` 초기값을 더 충분히 큰 수로 설정하세요.
- `2147483647` (21억) 또는 `int(1e9)` 등을 추천합니다.
- Python에서는 `import sys` 후 `sys.maxsize`를 사용하면 가장 안전합니다.

이 부분만 수정하면 정답을 받을 수 있을 것입니다! 고생하셨습니다.
"""
