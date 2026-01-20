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

"""
=== 백준 18111번 코드 리뷰 ===

[문제 이해]
- N x M 크기의 땅을 평평하게 고르는 작업입니다.
- 블록 제거는 2초, 놓기는 1초가 소요됩니다.
- 최소 시간과 그때의 땅 높이를 구해야 합니다.

[현재 접근 방식]
- 입력받은 땅의 높이를 `hash_table` (빈도수 배열)에 저장하여 O(NM)을 처음에만 수행하고,
- 이후 높이 탐색(0~256)에서는 O(257^2)로 최적화하셨습니다.
- 매우 훌륭한 접근입니다! N, M이 500이라도 충분히 빠릅니다.

[분석 결과]
- 시간 복잡도: O(N*M + H^2) (H=256) -> 통과 예상
- 로직 정확성: **치명적인 오류 발견**
- `dig_block` 변수 계산 시 `2 * ...`를 곱해서 '시간'을 계산하고 있는데,
- 38번 줄에서 이 값을 그대로 `available_block` (인벤토리)에 더하고 있습니다.
- 인벤토리에는 '시간'이 아니라 '제거한 블록의 개수'가 들어가야 합니다.

[힌트]
💡 변수의 의미를 다시 확인해보세요.
- `dig_block`은 현재 '시간(Cost)'을 담고 있습니다.
- 인벤토리(`available_block`)에 더해야 하는 값은 순수한 '블록 개수'여야 합니다.
- 36번 줄에서 시간 계산과 블록 개수 계산을 분리하거나, 38번 줄에서 2로 나누어 더해야 합니다.

[더 알아보면 좋을 것]
- Python 3에서는 `sys.stdin.readline`을 쓰더라도 Pypy3로 제출하는 것이 더 안전할 때가 많습니다.
- 높이 탐색 범위를 `min_height` ~ `max_height`로 더 좁힐 수도 있습니다.
"""

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
