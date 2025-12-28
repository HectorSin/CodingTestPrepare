# [문제 분석]
# 문제 링크: https://www.acmicpc.net/problem/10989 (수 정렬하기 3)
#
# [중요 제약 사항]
# 1. N의 크기: 최대 10,000,000 (천만)
# 2. **메모리 제한: 8MB** (매우 엄격함)
# 3. 수의 범위: 1 ~ 10,000
#
# [현재 코드 분석 및 피드백]
# 1. 메모리 초과 (Memory Limit Exceeded) 위험:
#    - 현재 코드는 `list(...)`를 사용하여 모든 입력을 메모리에 저장합니다.
#    - Python의 int는 객체로 취급되어 약 28바이트를 차지하며, 리스트 오버헤드까지 포함하면
#      10,000,000개의 정수를 저장하는 데 수백 MB가 필요합니다.
#    - 이는 8MB 제한을 즉시 초과하게 됩니다.
#
# 2. 성능 최적화 필요:
#    - `input()`은 대량의 입력 처리에 느릴 수 있습니다. `sys.stdin.readline` 사용을 권장합니다.
#
# [개선 제안: 계수 정렬 (Counting Sort)]
# - 수의 범위가 10,000으로 작다는 점을 이용합니다.
# - 크기가 10,001인 리스트를 만들어, 각 숫자가 등장할 때마다 카운트를 1씩 증가시킵니다.
# - 입력을 리스트에 당지 않고, 들어오는 즉시 카운팅만 수행하면 메모리를 매우 적게 사용합니다.
#
# [개선된 코드 예시]
# count = [0] * 10001
# N = int(sys.stdin.readline())
#
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     count[num] += 1
#
# for i in range(10001):
#     if count[i] != 0:
#         for _ in range(count[i]):
#             print(i)

# sys.stdin.readline 함수를 input 변수에 할당 (괄호 없이)

import sys

input = sys.stdin.readline

count = [0] * 10001

N = int(input())

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)