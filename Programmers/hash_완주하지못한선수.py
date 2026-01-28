def solution(participant, completion):
    sorted_parti = sorted(participant)
    sorted_comp = sorted(completion)

    answer = ''
    
    completion = False
    for i in range(len(sorted_parti)-1):
        if sorted_parti[i] != sorted_comp[i]:
            answer = sorted_parti[i]
            completion = True
    
    if not completion:
        answer = sorted_parti[-1]

    return answer

"""
=== 코드 리뷰 및 피드백 ===

[문제 이해]
- 완주하지 못한 선수를 찾는 문제입니다. (프로그래머스 '완주하지 못한 선수'로 추정)

[현재 접근 방식]
- 정렬(Sort) 후 순차 비교하는 방식을 사용했습니다.

[분석 결과]
- 시간 복잡도: O(N log N)
- 정확성: ⚠️ 오류 발생 가능성 있음
  - 중간에서 완주하지 못한 선수를 찾았을 때, 반복문을 멈추지(break) 않아서 이후의 값으로 덮어씌워질 수 있습니다.
  - 예: p=[A, B, C, D], c=[A, C, D] 일 때, B가 답이지만 C로 반환됩니다.
- 코드 스타일:
  - 매개변수 `completion`을 내부 변수(Boolean)로 덮어쓰고 있어 혼동을 줄 수 있습니다.

[힌트]
💡 논리 오류 수정이 필요합니다
- 다른 값을 찾으면 답을 저장한 후 즉시 반복문을 종료(`break`)해야 합니다.

💡 효율성 개선 (Level 2)
- 정렬을 하지 않고 해결할 수 있는 방법이 있습니다.
- Python의 `collections.Counter`나 Hash Map(Dictionary)을 사용하면 O(N)으로 최적화할 수 있습니다.

[더 알아보면 좋을 것]
- Python `break` 문
- `collections.Counter`의 활용
"""


# collections.Counter 쓰는 방식
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# Hash Map 쓰는 방식
import collections

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    
    for p in participant:
        dic[hash(p)] = p
        temp += hash(p)
    
    for c in completion:
        temp -= hash(c)
    
    return dic[int(temp)]