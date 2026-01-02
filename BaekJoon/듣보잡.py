# https://www.acmicpc.net/problem/1764
# 문제 분석: N개의 '듣도 못한' 명단과 M개의 '보도 못한' 명단의 교집합을 구하는 문제입니다.
# 현재 접근: 두 개의 리스트를 만들고, 이중 반복문(혹은 in 연산자)을 통해 교집합을 찾고 있습니다.
# ⌛ 시간 복잡도 분석:
#   - N, M의 최대 크기는 500,000입니다.
#   - 리스트에서 `in` 연산은 O(길이)의 시간이 걸립니다.
#   - 현재 로직은 각 원소마다 리스트 전체를 탐색하므로, 최악의 경우 O(N * M)이 됩니다.
#   - 500,000 * 500,000 = 250,000,000,000 (2500억) 연산이 필요하여 시간 제한(2초)을 초과합니다.
#
# 💡 힌트 레벨 1: 탐색 시간을 줄일 수 있는 자료구조를 떠올려보세요. O(1)에 찾을 수 있다면 어떨까요?
# 💡 힌트 레벨 2: '집합'을 나타내는 파이썬의 자료구조가 있습니다.

# 2s, 256mb

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

# 📌 체크포인트: 리스트는 순서가 있지만, 탐색 속도가 느립니다.
# 중복이 없고 순서가 상관없다면 더 빠른 자료구조를 사용할 수 있습니다.
d_list = set() # 듣지 못한
b_list = set() # 보지 못한

for _ in range(N):
    # 📌 체크포인트: set 자료구조에는 append() 대신 add() 메서드를 사용해야 합니다.
    d_list.add(input().rstrip())

for _ in range(M):
    b_list.add(input().rstrip())

# 💡 꿀팁: 두 집합의 공통된 원소(교집합)는 반복문 없이 '&' 연산자나 intersection() 메서드로 한 번에 구할 수 있습니다.
result = d_list & b_list

print(len(result))

for i in sorted(result):
    print(i)