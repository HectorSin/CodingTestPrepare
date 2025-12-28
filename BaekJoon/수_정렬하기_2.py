# [백준 2751번: 수 정렬하기 2](https://www.acmicpc.net/problem/2751)
# 
# [문제 분석]
# - 목표: N개의 수를 오름차순으로 정렬하여 출력
# - 제약 조건:
#   - N (1 ≤ N ≤ 1,000,000)
#   - 절댓값이 1,000,000보다 작거나 같은 정수 (중복 없음)
#   - 시간 제한: 2초
#   - 메모리 제한: 256MB

import sys

input = sys.stdin.readline

N = int(input())

numbers = []

for i in range(N):
    numbers.append(int(input()))
numbers.sort()

for num in numbers:
    print(num)