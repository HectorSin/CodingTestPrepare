# https://www.acmicpc.net/problem/30804

"""
2개의 input [1~200000] [1~9]과일 종류

과일을 input으로 받고 앞이든 되든 계속 pop 하면서 2개의 변수 저장
현재 어떤 과일인지 보다 몇개인지를 묻는 문제이기에 max_fruit 변수를 트랙킹하면 될 것으로 보임

자료형은 뒤에서부터 진행해도 되기에 list 사용
똑같이 aabb bbcc인 경우에도 단순 가장 많은 수인 4만 출력하면 되기에 순서 신경 X
만약 그런 규칙이 있다면 앞에서 진행하는지 뒤에서 진행하는지에 따라 따로 반영
"""

# 2s 1024mb

# N = int(input())

# fruit_list = list(map(int,input().split()))

# fruit_a = 0 # 과일 체크
# fruit_b = 0 # 과일 체크

# checker_a = 0 # 과일 개수 체크
# checker_b = 0 # 과일 개수 체크

# max_fruit = 0 # 최종 결과 변수

# first_setting = False

# for _ in range(N):
#     pop_fruit = fruit_list.pop()

#     if not first_setting:
#         if fruit_a == 0:
#             fruit_a = pop_fruit
#             checker_a += 1
#         else:
#             if fruit_b == 0:
#                 if pop_fruit == fruit_a:
#                     checker_a += 1
#                 else:
#                     fruit_b = pop_fruit
#                     checker_b += 1
#                     first_setting = True
    
#     # b와 같은 과일인지 체크 / 다르다면 max_fruit 반영 / 과일 변경
#     else:
#         if pop_fruit == fruit_b:
#             checker_b += 1
#         else:
#             if pop_fruit == fruit_a:
#                 checker_a += 1
#                 fruit_a, fruit_b = fruit_b, fruit_a
#                 checker_a, checker_b = checker_b, checker_a
#             else:
#                 max_fruit = max(max_fruit, checker_a+checker_b)
#                 fruit_a = fruit_b
#                 checker_a = checker_b
#                 fruit_b = pop_fruit
#                 checker_b = 1

# max_fruit = max(max_fruit, checker_a + checker_b)

# print(max_fruit)

# 위 방식의 경우 변수 1개를 추가하면 해결가능해보이지만 피드백에 따라 알고리즘 수정

"""
=== 백준 30804번 코드 리뷰 ===

[문제 이해]
- 과일 탕후루: 배열에서 '연속된' 구간 중 과일의 종류가 2가지 이하인 가장 긴 구간의 길이를 구하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O
- 문제 분석 단계: 접근 방식은 좋으나, 엣지 케이스 고려가 부족합니다.
- 자료구조 선택 근거: pop()을 사용하여 뒤에서부터 처리하는 방식은 독창적이나, 이 문제에서는 '슬라이딩 윈도우'의 윈도우 축소 과정이 복잡해질 수 있습니다.

[현재 접근 방식]
- 스택에서 하나씩 꺼내며(역순 탐색), 두 가지 과일의 개수(checker_a, checker_b)를 관리합니다.
- 새로운 과일(제3의 과일)이 나올 경우, 이전 과일(fruit_b)의 개수를 그대로 가져가려 합니다(checker_a = checker_b).

[분석 결과]
- 시간 복잡도: O(N)
- 예상 결과: 틀림 (특정 반례에서 오답 발생)
- 이유: `checker_b`는 현재 윈도우 내의 '총 개수'이지, '마지막에 연속된 개수'가 아닙니다.
  - 예: `1 2 1 2 3` (역순: `3 2 1 2 1`)
  - `1 2 1 2`까지는 a=1(2개), b=2(2개) 저장.
  - `3`이 들어올 때, 기존 윈도우 `1 2 1 2`에서 `2`만 남기려고 하면, 마지막 `2` 1개만 남아야 하는데, 코드에서는 `checker_b`(2개)를 모두 가져갑니다.

[힌트]
💡 연속된 구간을 관리하는 전형적인 "투 포인터 (Two Pointers)" 문제입니다.
- 왼쪽(left)과 오른쪽(right) 인덱스를 사용하여 윈도우를 늘리고 줄여보세요.
- 과일의 '종류'가 3개가 되면, 2개가 될 때까지 left를 이동시키는 방식이 훨씬 직관적입니다.
- 각 과일의 개수를 세기 위해 `Dictionary`나 `Counter`를 활용하면 좋습니다.

[설계 개선 제안]
다음 구조로 다시 설계해보세요:
1. `left`, `right` 포인터를 0에서 시작.
2. `right`를 늘려가며 과일 카운트 증가.
3. 과일 종류가 2개를 초과하면, 2개 이하가 될 때까지 `left`를 이동하며 카운트 감소.
4. 매 단계마다 `right - left + 1`의 최댓값 갱신.

[더 알아보면 좋을 것]
- 투 포인터(Two Pointers) 알고리즘
- 슬라이딩 윈도우(Sliding Window)
"""

# # 2s 1024mb
# from collections import Counter

# N = int(input())

# fruit_list = list(map(int,input().split()))

# start = 0
# end = 0

# max_fruit = 0

# def check_fruit(fruit_list, start, end):
#     """
#     과일 변수를 받아 2개인지 3개 이상인지 체크   
#     """
#     if len(Counter(fruit_list[start:end+1])) <= 2:
#         return True
#     else:
#         return False

# for _ in range(N-1):
#     end += 1

#     if not check_fruit(fruit_list, start, end):
#         while not check_fruit(fruit_list, start, end):
#             start += 1
    
#     max_fruit = max(max_fruit,(end - start + 1))

# print(max_fruit)

"""
=== 백준 30804번 코드 리뷰 ===

[문제 이해]
- 과일 탕후루: 연속된 구간에서 과일 종류가 2개 이하인 가장 긴 길이를 구함.

[설계 프로세스 평가]
- 주석 작성 여부: X (이전 피드백 후 바로 코드로 구현)
- 문제 분석 단계: 투 포인터 접근 방식은 아주 좋습니다.
- 설계-구현 일치도: 투 포인터 로직을 정확히 구현하려 했으나, 효율성에서 문제가 있습니다.

[현재 접근 방식]
- `start`, `end`를 이용한 슬라이딩 윈도우.
- 매 윈도우마다 `check_fruit` 함수에서 `Counter(slice)`를 호출하여 과일 종류 개수를 셉니다.

[분석 결과]
- 시간 복잡도: O(N^2)
  - `fruit_list[start:end+1]` 슬라이싱과 `Counter` 생성은 O(Window Size) 즉, O(N)입니다.
  - 이를 반복문 안에서 수행하므로 전체 복잡도는 O(N^2)가 됩니다.
  - N=200,000일 때 시간 초과(Time Limit Exceeded)가 발생합니다.
- 예상 결과: 시간 초과

[힌트]
💡 매번 `Counter`를 새로 만들지 말고, 딕셔너리 하나를 계속 유지하세요.
- `end`가 이동할 때: 딕셔너리에 해당 과일 카운트 추가 (+1)
- `len(dic)`이 3 이상일 때: `start`가 이동하며 딕셔너리에서 해당 과일 카운트 감소 (-1). 카운트가 0이 되면 딕셔너리에서 제거(`del`).
- 이렇게 하면 매 단계 연산량이 O(1)이 되어 전체 O(N)으로 통과할 수 있습니다.

[설계 개선 제안]
1. `nums = Counter()` (또는 `defaultdict`) 하나 생성
2. For문으로 `right` 이동: `nums[fruit[right]] += 1`
3. `len(nums) > 2` 일 동안 While문:
   - `nums[fruit[left]] -= 1`
   - `if nums[fruit[left]] == 0: del nums[fruit[left]]`
   - `left += 1`
4. `max_len` 갱신

[더 알아보면 좋을 것]
- Dictionary의 `del` 연산 시간 복잡도 (O(1))
"""


# 2s 1024mb
from collections import defaultdict

N = int(input())

fruit_list = list(map(int,input().split()))

fruit_counts = defaultdict(int)

left = 0
max_fruit = 0

for right in range(N):
    fruit_counts[fruit_list[right]] += 1

    while len(fruit_counts) > 2:
        fruit_counts[fruit_list[left]] -= 1

        if fruit_counts[fruit_list[left]] == 0:
            del fruit_counts[fruit_list[left]]
        
        left += 1
    
    max_fruit = max(max_fruit, right - left + 1)

print(max_fruit)

"""
=== 백준 30804번 코드 리뷰 ===

[문제 이해]
- 과일 탕후루: 연속된 구간에서 과일 종류가 2개 이하인 가장 긴 길이를 구함.

[설계 프로세스 평가]
- 주석 작성 여부: X (피드백 반영 반복으로 생략됨)
- 설계-구현 일치도: 완벽
- 개선 여부: 이전 O(N^2) 접근 방식에서 O(N)으로 성공적으로 개선했습니다.

[현재 접근 방식]
- `defaultdict`를 사용하여 현재 윈도우 내의 과일 종류별 개수를 관리.
- `right`를 늘리며 카운트 증가, 종류가 2개를 초과하면 `left`를 줄이며 카운트 감소 및 `del`.
- 투 포인터(Two Pointers) 알고리즘을 정석대로 구현했습니다.

[분석 결과]
- 시간 복잡도: O(N)
  - `right`가 0부터 N까지 1회 이동한다고 할 때, `left`는 최대 N번 이동합니다.
  - 각 단계에서 딕셔너리 접근은 평균 O(1)입니다.
  - 따라서 전체 시간 복잡도는 O(N)으로, N=200,000 입력에 대해 충분히 통과합니다.
- 예상 결과: 통과

[힌트]
💡 아주 훌륭하게 해결하셨습니다!
- `defaultdict`와 `del`을 적절히 사용하여 시간 복잡도를 획기적으로 줄였습니다.
- 이 패턴(슬라이딩 윈도우 + 해시맵)은 코딩 테스트에서 매우 자주 나오는 유형이니 잘 기억해두시면 좋습니다.

[더 알아보면 좋을 것]
- (선택) 입력 속도 최적화: `import sys; input = sys.stdin.readline` 사용 (Python에서 대량의 입력 처리 시 필수 테크닉 중 하나입니다)
"""