# 큐 데이터에서 우선순위에 따라 데이터를 빼고 더하는 방식으로 진행
# 즉 정렬하는 문제인데, 여기서 문제는 insert와 delete가 혼합된 방식이라 insert가 중복적으로 나타날 수 있다는 것이다.

# 간단하게 떠오르는 방식은 list로 q를 생성하고 첫 인덱스와 마지막 인덱스를 구하는 방식
# 결국 모든 과정이 끝난 후 sort 단 한번 진행하면 됨

# import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     k = int(input())
    
#     q = list()
#     start_index = 0
#     end_index = 0
    
#     for _ in range(k):
#         method, num = input().split()
#         num = int(num)
        
#         if method == "I":
#             q.append(num)
#         elif method == "D":
#             if end_index + start_index + 1 <= len(q):
#                 if num == 1:
#                     end_index += 1
#                 elif num == -1:
#                     start_index += 1
    
#     q.sort()
    
#     if len(q) == start_index + end_index:
#         print("EMPTY")
#     else:
#         print(q[-end_index], q[start_index])

"""
=== 백준 7662번 코드 리뷰 ===

[문제 이해]
- 이 문제는 데이터를 삽입하고, 현재 남아있는 데이터 중 최댓값 또는 최솟값을 삭제하는 '이중 우선순위 큐'를 구현하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O
- 문제 분석 단계: 보완 필요 (연산 순서가 무시되는 문제)
- 자료구조 선택 근거: 명확함 (단, 문제의 요구사항을 완벽히 충족하지 않음)
- 알고리즘 설계: 구체적
- 설계-구현 일치도: 일치

[현재 접근 방식]
- 데이터를 리스트에 전부 추가한 뒤, 삭제 개수만(start_index, end_index) 카운팅하고 모든 연산이 끝난 후 단 한 번 정렬하여 양쪽 끝에서 결과를 도출하는 방식을 사용하고 있습니다.

[분석 결과]
- 시간 복잡도: O(K log K)
- 공간 복잡도: O(K)
- 예상 결과: 틀림
- 이유: 모든 삽입/삭제가 실시간으로 반영되어야 합니다. 현재 로직은 연산 순서를 무시하고 나중에 한 번만 정렬하여 자르기 때문에, 삭제 연산 시점의 최댓값/최솟값이 아닌 전체 누적 데이터 상의 최댓값/최솟값이 지워지게 되어 정확한 결과를 낼 수 없습니다.

[힌트]
💡 삭제가 일어나는 "시점"의 상태에 따라 알맞은 값을 제거해야 합니다!
- 삽입/삭제 시마다 리스트를 `sort()` 하거나 탐색하면 O(K)가 시도되어 전체 O(K^2)으로 100% 시간 초과가 발생합니다 (K=1,000,000).
- 데이터를 넣을 때 최솟값, 최댓값을 항상 빠르게(O(log N)) 찾을 수 있는 자료구조는 무엇이 있을까요?
- 최댓값을 찾는 자료구조와 최솟값을 찾는 자료구조 2개를 동시에 운용해볼 수는 없을까요?
- 만약 2개를 운용한다면, 한 곳에서 삭제된 데이터가 다른 곳에도 삭제되었음을 어떻게 알릴지 고민해보세요.

[설계 개선 제안]
다음 구조로 주석의 설계를 개선해보세요:
1. 삽입, 최댓값 삭제, 최솟값 삭제 연산을 각각 언제/어떻게 처리할 것인가?
2. 최댓값과 최솟값을 양방향에서 빠르게 빼주기 적합한 자료구조 조합 선택
3. 삭제된 노드를 추적하는 방법 (이미 지워진 값인지 확인하는 장치 필요 유무)

[더 알아보면 좋을 것]
- 최소 힙(Min Heap) 과 최대 힙(Max Heap) (`heapq` 모듈 응용)
- 지연 삭제(Lazy Deletion) 기법 혹은 식별자(ID)를 통한 상태(True/False) 관리
"""

# # 위 피드백을 반영해서 파이썬의 최소힙 & 최대힙을 활용해서 해당 문제 해결

# from heapq import heappush, heappop

# import sys

# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     k = int(input())
    
#     max_q = []
#     min_q = []
    
#     len_list = 0
    
#     for _ in range(k):
#         method, num = input().split()
#         num = int(num)
        
#         if method == "I":
#             heappush(min_q, num)
#             heappush(max_q, (-num, num))
#             len_list += 1
#         elif method == "D":
#             if len_list > 0:
#                 len_list -= 1
#                 if num == 1:
#                     heappop(max_q)
#                 elif num == -1:
#                     heappop(min_q)
    
#     if len_list == 0:
#         print("EMPTY")
#     else:
#         print(heappop(max_q)[1], heappop(min_q))

"""
=== 백준 7662번 코드 리뷰 (2차) ===

[설계 프로세스 평가]
- 힙을 두 개(최대 힙, 최소 힙) 사용하는 핵심 아이디어에 아주 잘 접근하셨습니다.

[현재 접근 방식]
- `max_q`와 `min_q`를 생성하고, `len_list`로 전체 큐의 크기를 추적합니다. 삭제 연산 시 각각의 힙에서 단순히 `pop`을 수행하여 처리를 시도하고 있습니다.

[분석 결과]
- 시간 복잡도: O(K log K)
- 예상 결과: 틀림
- 이유: 한쪽 힙에서 삭제된 원소가 다른 쪽 힙에는 그대로 남아있게 되는 **동기화 문제**가 발생합니다.
- 반례 상황:
  1. I 10, I 20 삽입 (max_q: 20, 10 / min_q: 10, 20)
  2. D 1 (최댓값 20 삭제. max_q에서 20이 제거되나 min_q에는 20이 남아있음)
  3. D -1 (최솟값 10 삭제. min_q에서 10이 제거되나 max_q에는 10이 남아있음)
  => 현재 `len_list`는 0이지만, `max_q`에는 10, `min_q`에는 20이 유령 데이터로 남아있습니다!
  4. I 40 삽입 (max_q: 40, 10 / min_q: 20, 40)
  5. D -1 (최솟값 삭제 시, 실제로 40이 삭제되어야 하지만 min_q에서 예전 유령 데이터인 20이 pop됩니다)

[힌트]
💡 두 힙 사이에서 "어떤 원소가 이미 삭제되었는지" 알려주는 장치가 필요합니다.
- 단순 길이 연산(`len_list`)만으로는 한쪽 힙에서 무엇이 삭제되었는지 맞은편 힙이 알 방법이 없습니다.
- 각 삽입(I) 과정마다 고유한 **식별자(ID)** (예: 반복문의 인덱스 `i`)를 함께 튜플로 묶어서 힙에 넣어보면 어떨까요?
- 그리고 크기가 `k`인 불리언(Boolean) 배열 `visited`나 `deleted`를 만들어서 특정 ID가 삭제되었다면 `True`로 표시해두는 겁니다.
- 힙에서 데이터를 꺼낼 때(또는 결과를 출력하기 전에), 꺼낸 데이터의 ID가 이미 `visited` 배열에서 `True`로 처리된 데이터라면, 그것은 '상대방 힙에서 이미 지운 유령 데이터'이므로 가차없이 버리고(계속 pop) 진짜 데이터를 찾을 때까지 반복(Lazy Deletion)해주어야 합니다.

[설계 개선 제안]
- 큐에 삽입 시: `(값, ID)` 형태 저장
- 최댓값/최솟값 삭제 시: 힙의 루트 노트가 '이미 삭제된 ID' 인지 반복문(`while`)으로 확인 후 제거. 유효한 ID를 찾으면 해당 ID를 삭제 처리(`visited[id] = False`).
- 모든 연산 종료 후: 출력 전에도 양쪽 힙에 남아있는 유령 데이터들을 한 번 더 청소해 주어야 쓰레기값이 안 나옵니다.
"""


from heapq import heappush, heappop

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    
    max_q = []
    min_q = []
    
    hash_table = [False] * (k+1)
    
    len_list = 0
    
    for i in range(k):
        method, num = input().split()
        num = int(num)
        
        if method == "I":
            heappush(min_q, (num, i))
            heappush(max_q, (-num, num, i))
            len_list += 1
        elif method == "D":
            if len_list > 0:
                len_list -= 1
                if num == 1:
                    while max_q:
                        check_num = heappop(max_q)
                        if hash_table[check_num[2]] == False:
                            hash_table[check_num[2]] = True
                            break
                            
                elif num == -1:
                    while min_q:
                        check_num = heappop(min_q)
                        if hash_table[check_num[1]] == False:
                            hash_table[check_num[1]] = True
                            break
    
    if len_list == 0:
        print("EMPTY")
    else:      
        while max_q:
            max_num = heappop(max_q)
            if hash_table[max_num[2]] == False:
                break
        
        max_num = max_num[1]
        
        if len_list == 1:
            min_num = max_num
        else:
            while min_q:
                min_num = heappop(min_q)
                if hash_table[min_num[1]] == False:
                    break
            min_num = min_num[0]
    
        print(max_num, min_num)