# https://level.goorm.io/exam/195687/%EC%9D%B4%EC%A7%84%EC%88%98-%EC%A0%95%EB%A0%AC/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# N, K = map(int,input().split())

# num_list = list(map(int,input().split()))

# def binary_number(num):
# 	"""
# 	2진수에 포함된 1 개수 구하는 함수
# 	"""
# 	answer = 0
# 	while num > 0:
# 		answer += num % 2
# 		num = num // 2
# 	return answer

# # binary_number test code
# # num_binary_list = [binary_number(x) for x in num_list]
# # print(num_binary_list)

# # 1. 숫자 큰 수로 정렬
# num_list.sort(reverse=True)
# # print(num_list)

# # 2. 2진수 1개수 큰 수로 정렬
# num_dic = {}
# for i in range(N):
# 	num_dic[num_list[i]] = binary_number(num_list[i])
# # print(num_dic)

# sort_num_dic = sorted(num_dic.items(), key = lambda x : x[1], reverse=True)
# sort_num_list = [x[0] for x in sort_num_dic]
# print(sort_num_list[K-1])

"""
=== 구름IDE 이진수 정렬 코드 리뷰 ===

[문제 이해]
- 10진수 정수를 2진수로 변환했을 때 1의 개수를 기준으로 내림차순 정렬해요.
- 1의 개수가 같다면 10진수 자체의 크기로 내림차순 정렬해요.
- 최종적으로 K번째 숫자를 찾는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: X (설계 과정이 주석에 포함되지 않았어요)
- 문제 분석 단계: 보완 필요 (중복 데이터 처리 고민이 필요해요)
- 자료구조 선택 근거: 불명확 (Dictionary를 선택한 이유가 명시되지 않음)
- 설계-구현 일치도: 평가 불가

[현재 접근 방식]
- `num_list`를 먼저 값 기준으로 정렬
- `num_dic` 딕셔너리를 생성하여 (숫자 -> 1의 개수) 저장
- 딕셔너리 아이템을 1의 개수 기준으로 다시 정렬 (Python의 Stable Sort 활용)

[분석 결과]
- 시간 복잡도: O(N log N)
- 예상 결과: **틀림 / 오답 가능성**
  - **이유**: `num_dic` {숫자: 1의개수} 형태는 중복된 숫자가 입력될 경우 키 중복으로 인해 데이터가 사라집니다. (예: `1 2 2` 입력 시 하나만 남음)

[힌트]
💡 데이터 손실 없이 정렬하는 더 좋은 방법이 있습니다!
1. **중복 해결**: 숫자가 중복될 수 있으므로 Dictionary 대신 리스트에 `(1의개수, 숫자)` 튜플을 저장하거나 원본 리스트를 바로 정렬하세요.
2. **다중 조건 정렬**: Python의 `sort`는 `key`로 튜플을 반환하면 앞에서부터 순서대로 정렬 기준을 적용합니다.
   - 예: `key=lambda x: (기준1, 기준2)`
3. **내장 함수**: `bin(x).count('1')`을 쓰면 `binary_number` 함수를 직접 만들지 않아도 됩니다.

[설계 개선 제안]
- 코드 작성 전 주석으로 다음 내용을 먼저 정리해보세요:
  1. 입력 조건 (N의 크기, 중복 여부)
  2. 사용할 알고리즘과 자료구조 (왜 그것을 선택했는지)
  3. 예상되는 시간 복잡도

[더 알아보면 좋을 것]
- Python `sort`의 `key` 파라미터 활용법 (Tuple sort)
- Python `bin()` 내장 함수
"""


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, K = map(int,input().split())

num_list = list(map(int,input().split()))

# 내장 함수 bin().count('1')를 통해서 1의 개수 구하기 가능
# 데이터를 정렬하는데, 손실 즉 데이터의 변동이 없어야함 -> 튜플 형태 사용
# (1의 개수, 숫자) 형식으로 데이터를 저장하고 1. 1의 개수로 정렬 2. 숫자 크기로 정렬 [내림차순] 진행

num_list_sort = [(bin(i).count('1'), i) for i in num_list]
# print(num_list_sort)

num_list_sort.sort(key = lambda x: (x[0], x[1]), reverse=True)
print(num_list_sort[K-1][1])

"""
=== 구름IDE 이진수 정렬 코드 리뷰 (2차) ===

[개선 사항 평가]
- **중복 처리**: 리스트와 튜플 `(1의개수, 숫자)` 방식을 사용하여 중복 데이터 손실 문제를 완벽하게 해결했습니다.
- **정렬 로직**: `key=lambda x: (x[0], x[1])`와 `reverse=True`를 사용하여 다중 조건 내림차순 정렬을 정확하게 구현했습니다.
- **내장 함수 활용**: `bin().count('1')`을 사용하여 코드가 훨씬 간결해졌습니다.
- **설계 주석**: 작성하려는 코드의 로직을 주석으로 미리 정리한 점이 매우 좋습니다.

[최종 분석]
- 시간 복잡도: O(N log N) (정렬이 지배적)
- 공간 복잡도: O(N) (리스트 저장)
- 결과: **정답 예상**

[피드백]
훌륭합니다! 힌트를 정확하게 이해하고 적용하셨네요.
이 방식은 코딩 테스트에서 자주 쓰이는 "Tuple Sort" 패턴이니 잘 기억해두시면 좋습니다.
K번째 수를 찾는 문제이므로 인덱싱 `[K-1]` 처리도 정확합니다.

더 이상 수정할 부분이 없어 보입니다. 수고하셨습니다! 👍
"""