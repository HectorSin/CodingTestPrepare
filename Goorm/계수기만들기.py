# https://level.goorm.io/exam/43061/%EA%B3%84%EC%88%98%EA%B8%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N = int(input()) # 최대 8

A_list = list(map(int,input().split())) # 각 숫자판의 최댓값
B_list = list(map(int,input().split())) # 각 숫자판의 초기값
K = int(input())

# # 끝자리부터 각 수를 곱한값을 list 형태로 저장
# # 해당 값을 통해 1차적으로 각 자릿수에 더할 값 구함
# # 다 더한 후 자리 올려야 되는 수 더함

# hash_table = [0] * N
# hash_table[-1] = A_list[-1]
# for i in range(1,len(A_list)):
# 	hash_table[-i-1] = hash_table[-i] * A_list[-i-1]
# hash_table.append(1)
# print(hash_table)

# add_list = [0] * N

# for i in range(N):
# 	add_list[i] = K // hash_table[i+1]
# 	K = K % hash_table[i+1]
# # add_list[-1] = K

# print(add_list)

next_add = 0
# 그리디 방식으로 접근
for i in range(N-1,-1,-1):
	B_list[i] = B_list[i] + K
	K = B_list[i] // (A_list[i] + 1)
	B_list[i] = B_list[i] % (A_list[i]+1)

print(*B_list, sep="")


# 기존방식의 경우 시간 복잡도를 더 줄이기 위해 해쉬 테이블을 사용하는 방식으로 할려고 했으나 A_list를 나누는 것이 아닌 1을 더한 값으로 나눠야 하는데 이를 못함

"""
=== 구름LEVEL 계수기 만들기 코드 리뷰 ===

[문제 이해]
- 각 자리마다 최댓값(Base)이 다른 계수기에 K를 더한 결과를 구하는 문제입니다.
- 일반적인 진법(10진수, 2진수)이 아닌 혼합 기수(Mixed Radix) 시스템입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O (시도했던 흔적과 현재 접근 방식이 적혀있음)
- 문제 분석: 주석을 통해 해시 테이블(가중치 미리 계산) 방식과 현재 방식을 고민한 흔적이 보입니다.
- 자료구조/알고리즘: 리스트와 반복문을 이용한 자리 올림(Carry) 처리가 적절합니다.

[현재 접근 방식]
- 마지막 자리부터 역순으로 순회하며 K를 더하고, 자리 올림(Carry)을 K에 갱신하며 진행하는 방식입니다.
- `next_add` 변수는 선언만 되고 사용되지 않았습니다.

[분석 결과]
- 시간 복잡도: O(N) (N은 최대 8이므로 매우 효율적)
- 예상 결과: 통과
- 코드의 로직이 깔끔하고 불필요한 연산이 없습니다.

[힌트 & 피드백]
💡 아주 잘 해결하셨습니다!
- 현재 방식(O(N))이 가장 효율적이고 직관적입니다.
- 주석에 남기신 "해쉬 테이블 사용 방식"은 사실상 **"전체 값을 하나의 정수로 변환 -> K 더하기 -> 다시 각 자리로 변환"**하는 과정과 같습니다.
  - 이 방식도 가능하지만, 자릿수가 많아지면 전체 숫자가 매우 커질 수 있어 현재의 자릿수별 처리 방식이 오버플로우 위험(파이썬은 없지만)이나 메모리 측면에서 더 안전할 수 있습니다.
- "그리디 방식"이라는 표현보다는 **"구현(Implementation)"** 또는 **"시뮬레이션"**이 더 적절한 표현입니다.

[설계 개선 제안]
- 불필요한 주석(실패한 시도)과 사용하지 않는 변수(`next_add`)를 정리하면 코드가 더 깔끔해질 것입니다.
- 코드 상단에 문제의 핵심 조건(각 자리의 진법이 다름)을 명시하면 더 좋은 설계 문서가 됩니다.

[더 알아보면 좋을 것]
- 혼합 기수법(Mixed Radix System)에 대해 알아보시면 이 문제의 수학적 배경을 더 깊이 이해할 수 있습니다.
- `divmod()` 함수를 사용하면 몫과 나머지를 한 번에 구할 수 있어 코드를 더 간결하게 만들 수 있습니다.
  예: `K, B_list[i] = divmod(B_list[i] + K, A_list[i] + 1)`
"""