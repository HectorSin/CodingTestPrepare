# 문제: 백준 1920번 수 찾기 (https://www.acmicpc.net/problem/1920)
# 목표: N개의 정수 안에 X라는 정수가 존재하는지 M번 확인
# 제한: 정수의 범위가 -2^31 ~ 2^31로 매우 큽니다. (int 범위 전체)
# 시간 복잡도: O(M log N) 또는 O(M) 권장 (N, M <= 100,000)

import sys
input = sys.stdin.readline

N = int(input())

# N개의 정수 A[1]~
A_list = list(map(int,input().split()))

M = int(input())

M_list = list(map(int,input().split()))


"""
# 단순 시간 복잡도 O(N^2) -> 10,000,000,000 [1초 안에 불가 코드 수정 필요]
for i in range(M):
    if M_list[i] in A_list:
        print(1)
    else:
        print(0)
"""

# [치명적 오류 발견]
# 문제의 정수 범위는 -2^31 ~ 2^31입니다. (음수 포함, 매우 큰 수 가능)
# 현재 작성하신 `A_hash = [0] * 100001`은 0~100,000 범위의 수만 처리 가능하므로,
# 범위를 벗어나는 입력(음수나 10만 초과)이 들어오면 IndexError가 발생하거나 틀린 답이 나옵니다.

# [개선 방안: Set 자료구조 활용]
# List 대신 Set을 사용하면 탐색(in 연산)이 평균 O(1)입니다.
# 전체 시간 복잡도: O(N) (Set 생성) + O(M) (검색) = O(N+M)으로 매우 효율적입니다.
# 
# 수정 제안 코드:
# A_set = set(A_list)
# for num in M_list:
#     print(1 if num in A_set else 0)

"""
A_hash = [0] * 100001
for A in A_list:
    A_hash[A] += 1

for i in range(M):
    if A_hash[M_list[i]] > 0:
        print(1)
    else:
        print(0)
"""

A_set = set(A_list)
for num in M_list:
    print(1 if num in A_set else 0)

"""
결국 다시 초기 방식의 알고리즘으로 롤백 대신 Set를 활용하여 중복된 수를 줄이니 O(N^2)이 O(N+M)으로 변경
"""