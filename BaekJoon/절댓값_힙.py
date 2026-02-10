# 리스트 형태로 두개의 리스트를 저장 하나는 음수 하나는 양수
# 0이 나오기 전까지 단순 넣기
# 0이 나올때마다 정렬? [이때 연속적으로 0이나오면 정렬 X]
# 두 리스트 다 빈 경우 0출력


# import sys
# input = sys.stdin.readline

# N = int(input())

# pos_list = []
# neg_list = []

# need_sort = True

# for _ in range(N):
#     cal = int(input())

#     if cal == 0:
#         if not pos_list and not neg_list:
#             print(0)
#         else:
#             if need_sort:
#                 pos_list.sort(reverse=True)
#                 neg_list.sort()

#             if pos_list and not neg_list:
#                 pop_num = pos_list.pop()
#                 print(pop_num)
#             elif not pos_list and neg_list:
#                 pop_num = neg_list.pop()
#                 print(pop_num)
#             else:
#                 if abs(neg_list[-1]) <= abs(pos_list[-1]):
#                     pop_num = neg_list.pop()
#                     print(pop_num)
#                 else:
#                     pop_num = pos_list.pop()
#                     print(pop_num)
#         need_sort = False
#     else:
#         need_sort = True
#         if cal > 0:
#             pos_list.append(cal)
#         else:
#             neg_list.append(cal)


# 단순 그리드 방식으로 최악의 경우 시간초과

"""
=== 백준 11286번 코드 리뷰 ===

[문제 이해]
- 절댓값 힙: 절댓값이 가장 작은 값을 출력하고 제거
- 절댓값이 같으면 실제 값이 작은 것을 우선 출력
- 0 입력 시 최솟값 출력 및 제거, 비어있으면 0 출력

[설계 프로세스 평가]
- 주석 작성 여부: O (간단한 아이디어 메모)
- 문제 분석 단계: 보완 필요
- 자료구조 선택 근거: 불명확
- 알고리즘 설계: 추상적
- 설계-구현 일치도: 부분 불일치

[현재 접근 방식]
- 양수/음수를 별도 리스트로 관리
- 0 입력 시마다 정렬 후 pop
- need_sort 플래그로 불필요한 정렬 방지 시도

[분석 결과]
- 시간 복잡도: 
  * 최악의 경우 매 출력마다 정렬 → O(N × M log M)
  * N: 전체 연산 수, M: 리스트 크기 (최대 N)
  * N 최대 100,000 → 정렬 반복 시 시간 초과 가능
- 공간 복잡도: O(N)
- 예상 결과: 시간 초과 가능성 높음

[힌트]
💡 "힙(Heap)"이라는 문제 제목에 주목해보세요
- Python에는 힙 연산을 O(log N)에 처리하는 표준 라이브러리가 있습니다
- 정렬(O(N log N))보다 훨씬 빠른 방법입니다
- 절댓값 비교를 위한 "우선순위" 설정 방법을 고민해보세요

[설계 개선 제안]
다음 번 문제를 풀 때는 코드 작성 전에 이런 구조로 설계해보세요:

```
[문제 핵심]
- 동적으로 최솟값을 빠르게 찾고 제거해야 함
- "힙" 자료구조가 이런 작업에 최적화되어 있음

[자료구조 선택]
- heapq 모듈 사용 (Min Heap)
- 절댓값 기준 정렬을 위한 튜플 활용: (절댓값, 원래값)

[알고리즘]
1. 삽입: heappush((abs(x), x))
2. 삭제: heappop()으로 O(log N)에 최솟값 추출
3. 빈 힙 체크 후 0 또는 값 출력

[복잡도]
- 시간: O(N log N) - 각 연산이 O(log N)
- 공간: O(N)
```

[더 알아보면 좋을 것]
- heapq 모듈 (우선순위 큐)
- 힙 자료구조의 특성 (완전 이진 트리)
- 튜플 비교 규칙 (첫 번째 원소 우선, 같으면 두 번째 비교)
- 문제 제목이 힌트인 경우가 많습니다!

[긍정적인 부분]
✅ need_sort 플래그로 최적화 시도 - 좋은 사고방식입니다
✅ 엣지 케이스 처리 (빈 리스트, 한쪽만 있는 경우)
✅ 시간 복잡도 문제를 스스로 인지 (주석 50번 줄)
"""

import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    cal = int(input())
    if cal == 0:
        if heap:
            pop_num = heapq.heappop(heap)
            print(pop_num[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(abs(cal),cal))

# print(heap)

