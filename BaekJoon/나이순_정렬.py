# 문제: 백준 10814번 나이순 정렬 (https://www.acmicpc.net/problem/10814)
# 목표: 나이순으로 정렬하되, 나이가 같으면 가입한 순서(입력 순서)를 유지 (Stable Sort)
# 시간 복잡도: O(N log N) (N <= 100,000, 3초 제한으로 충분함)
# 공간 복잡도: O(N) (256MB 제한으로 충분함)

import sys

# [입력 속도 개선] N이 10만 단위이므로 input() 대신 sys.stdin.readline을 사용하는 것이 좋습니다.
input = sys.stdin.readline

# N = int(sys.stdin.readline())
N = int(input())

# [메모리 확인] 답변: 네, 충분합니다.
# N=100,000일 때, 각 데이터가 (int, string) 튜플이어도 
# 수십 MB 내외로 256MB 제한보다 훨씬 적게 사용합니다.

people_list = []

for i in range(N):
    age, name = input().split()
    people_list.append((int(age), name))

# [Stable Sort] Python의 기본 sort는 Stable Sort입니다.
# 즉, 키(나이)가 같으면 기존 리스트의 순서(가입 순서)가 유지되므로 문제 조건에 딱 맞습니다.
people_list.sort(key=lambda x:x[0])

for people in people_list:
    print(people[0], people[1])