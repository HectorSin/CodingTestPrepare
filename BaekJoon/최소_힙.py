"""
https://www.acmicpc.net/problem/1927
"""

# 1s, 128mb
# 조건: 0 -> 가장 작은수 pring & 해당 수 배열에서 제거
# 조건2: 배열이 비어있는데 0이 온 경우 0 출력


# 문제 분석: 
# N개의 연산(최대 100,000)을 처리해야 하며, 자연수를 입력받으면 배열에 넣고 0을 입력받으면 최솟값을 출력/제거해야 합니다.
# 중요한 점은 입력되는 자연수 x의 범위가 0 ~ 2^31-1로 매우 크다는 것입니다.

# 현재 접근: 
# 입력값 x를 인덱스로 사용하는 리스트(n_hash)를 만들고 있습니다.
# 이 방식은 x가 클 경우(예: 21억) 리스트의 크기도 21억이 되어야 하므로
# 128MB 메모리 제한을 초과하게 됩니다 (Memory Limit Exceeded).

# 힌트 레벨 1: 
# 모든 수의 범위를 커버하는 배열 대신, 현재 들어있는 수들만 관리하는 자료구조가 필요합니다.
# '최소 힙(Min Heap)' 자료구조를 사용하면 원소 추가와 최솟값 삭제를 O(log N) 시간에 처리할 수 있습니다.
# 파이썬의 표준 라이브러리인 `heapq`를 사용해보세요.


"""
import sys
import heapq # 힌트: 이 모듈을 활용해보세요

input = sys.stdin.readline

trial = int(input())

n_hash = []

for _ in range(trial):
    in_data = int(input())

    if in_data != 0:
        # 💡 힌트 레벨 2: 여기에 heappush를 사용하세요
        # 기존: n_hash 리스트를 늘리고 카운트 증가
        # 변경: heapq.heappush(heap_list, in_data)
        if len(n_hash) < in_data+1:
            for _ in range(in_data - len(n_hash) + 1):
                n_hash.append(0)
        n_hash[in_data] += 1
    else:
        # 💡 힌트 레벨 2: 여기에 heappop을 사용하세요
        # 배열이 비어있는지 확인하려면 if not heap_list: ... logic 사용
        # 비어있지 않다면 print(heapq.heappop(heap_list))
        success = False
        for i in range(len(n_hash)):
            if n_hash[i] != 0:
                print(i)
                n_hash[i] -= 1
                success = True
                break
        
        if not success:
            print(0)
"""


# 피드백 반영 - 파이썬 패키지 heapq - 최소 힙 구조를 활용하여 해결 [heappush, heappop]
import sys
import heapq

input = sys.stdin.readline

trial = int(input())

heap_list = []

for _ in range(trial):
    in_data = int(input())

    if in_data != 0:
        heapq.heappush(heap_list, in_data)
    else:
        if not heap_list:
            # 비어 있는 경우
            print(0)
        else:
            print(heapq.heappop(heap_list))