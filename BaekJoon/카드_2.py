# 1~N까지의 카드
# [백준 2164번: 카드2](https://www.acmicpc.net/problem/2164)
# 
# [문제 분석]
# 1. 입력 조건: N은 최대 500,000입니다.
# 2. 시간 제한: 2초.
#    - Python에서 1초당 약 2,000만~1억 번의 연산이 가능하다고 가정하면, 
#    - O(N^2) 알고리즘은 500,000^2 = 2,500억 번의 연산이 필요하므로 2초를 훨씬 초과합니다.
#    - 따라서 반드시 O(N) 또는 O(N log N) 이하의 알고리즘을 사용해야 합니다.
#
# [현재 코드의 문제점: 시간 초과(TLE)]
# - Python의 list.pop(0)은 첫 번째 요소를 제거한 뒤, 나머지 모든 요소를 앞으로 한 칸씩 당겨오는 연산(Shift)을 수행합니다.
# - 이 연산의 시간 복잡도는 O(len(list))입니다.
# - 위 작업을 N번 반복하므로 전체 시간 복잡도는 O(N^2)가 되어 시간 초과가 발생합니다.
#
# [개선 방안]
# - collections 모듈의 deque를 사용하세요.
# - deque.popleft()는 O(1)의 시간 복잡도를 가집니다.
# - 이를 사용하면 전체 로직을 O(N)으로 처리할 수 있어 500,000개 입력도 0.5초 이내에 충분히 처리가 가능합니다.

"""
[기존 코드 분석 및 답변]
Q: 문제에서 어떤걸 봤으면 이걸 미리 예상했을 수 있을까?
A: 
1. **N의 크기 (500,000)**: 
   - 보통 N이 10만을 넘어가면 O(N^2) 로직은 사용할 수 없습니다. O(N)이나 O(N log N)을 목표로 해야 합니다.
2. **동작의 특성 (앞에서 빼고 뒤로 넣기)**:
   - '앞에서 빼는' 동작이 빈번하게 일어나는 경우, Python의 List는 적합하지 않습니다. (pop(0) 비용 발생)
   - 'Queue' 자료구조가 필요한 전형적인 문제입니다.

# [기존 (느린) 코드 보존]
card_list = []
for i in range(N):
    card_list.append(i+1)

while True:
    if len(card_list) == 1:
        break
    card_list.pop(0) # 여기서 O(N) 발생 -> 전체 O(N^2)
    second_card = card_list.pop(0)
    card_list.append(second_card)

print(card_list[0])
"""

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

que = deque(range(1,N+1))

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])