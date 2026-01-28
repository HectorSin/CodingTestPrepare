# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    cloth_hash = {}
    
    for cl in clothes:
        if cl[1] not in cloth_hash:
            cloth_hash[cl[1]] = []
        cloth_hash[cl[1]].append(cl[0])
    
    trial = 1
    for ch in cloth_hash:
        trial = trial * (len(cloth_hash[ch])+1)
    return trial - 1

"""
=== 프로그래머스 의상 코드 리뷰 ===

[문제 이해]
- 서로 다른 옷의 조합의 수를 구하는 문제입니다.
- 각 종류별로 최대 1가지만 착용 가능하며, 최소 1개 이상의 옷을 입어야 합니다.

[현재 접근 방식]
- 해시(Dictionary)를 사용하여 옷의 종류별로 리스트를 만들어 분류하고 있습니다.
- (각 종류별 개수 + 1)을 모두 곱한 뒤, 아무것도 입지 않은 경우(1)를 빼는 방식을 사용했습니다.

[분석 결과]
- 시간 복잡도: O(N) (N: 옷의 개수)
  - 딕셔너리 구성에 O(N), 종류별 계산에 O(K)가 소요되어 효율적입니다.
- 공간 복잡도: O(N)
  - 옷의 이름을 리스트에 저장하므로 O(N) 공간을 차지합니다.
- 예상 결과: 통과 (정확성 및 효율성 좋음)

[힌트]
💡 정말 잘 짜셨습니다! 로직이 정확합니다. 조금 더 최적화할 수 있는 부분을 알려드릴게요.
- 옷의 '이름'은 계산식에서 사용되지 않고, '개수'만 필요합니다.
- 따라서 리스트에 이름을 저장하는 대신, 개수(int)만 카운팅하면 메모리를 절약할 수 있습니다.
- Python의 `collections.Counter`를 사용하면 for문 없이 의상 종류별 개수를 쉽게 구할 수 있습니다.
- `reduce` 함수를 활용하면 곱셈 연산도 한 줄로 처리할 수 있습니다.

[더 알아보면 좋을 것]
- collections.Counter
- functools.reduce
"""

"""
[Tips] collections.Counter를 활용한 구현 예시
"""
from collections import Counter
from functools import reduce

def solution_with_counter(clothes):
    # 1. 의상 종류(type)별 개수 세기
    # cloth[1]이 의상의 종류입니다.
    counts = Counter([type for name, type in clothes])
    
    # 2. 각 종류별 (개수 + 1)을 모두 곱하기
    # reduce(함수, 순회가능한데이터, 초기값)
    # 초기값 1에다가 (각 종류 개수 + 1)을 계속 곱해나갑니다.
    answer = reduce(lambda x, y: x * (y + 1), counts.values(), 1)
    
    # 3. 아무것도 입지 않는 경우 1 빼기
    return answer - 1