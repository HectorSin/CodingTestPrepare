import sys
# 문제: 백준 18110번 solved.ac (https://www.acmicpc.net/problem/18110)
#
# [문제 분석]
# 1. 입력: 첫 줄 N(0~30만), 그 뒤로 난이도 의견 N개.
# 2. 로직: 절사평균(상하위 15% 제외)을 구하되, '사사오입' 반올림 적용.
# 3. 엣지 케이스: N=0인 경우 '0'을 출력해야 함.
#
# [코드 분석 & 피드백]
# [코드 분석 & 피드백 (2차)]
# 1. 반올림 수정: `int(x + 0.5)` 방식으로 사사오입을 잘 구현하셨습니다. 정답 로직입니다.
# 2. 치명적인 실수 발견: `sys.exit` 뒤에 괄호 `()`가 없습니다.
#    - `sys.exit` 자체는 함수 객체일 뿐, 프로그램이 종료되지 않습니다.
#    - **반드시** `sys.exit()` 형태로 호출해야 프로그램이 즉시 종료됩니다.
#    - 이게 없으면 n=0일 때 `num_que`가 비어있어, 마지막 줄에서 `ZeroDivisionError`가 발생합니다.
# 3. 효율성: 정렬과 deque 사용 방식은 O(NlogN)으로 적절합니다.

# 1s 1024mb
import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) # 1~300000

if n == 0:
    print(0)
    sys.exit()

num_list = []

# O(N)
for _ in range(n):
    num_list.append(int(input()))

# O(NlogN)
num_list.sort()
num_que = deque(num_list)

# 몇개를 빼야하는지 15% 범위
erase_range = int(n*0.15 + 0.5)

for _ in range(erase_range):
    num_que.popleft()
    num_que.pop()

print(int((sum(num_que)/len(num_que))+0.5))