# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 팩터리얼 계산이 여러번 들어감 즉 한번 계산과정을 저장하는 방식 사용 필요해보임
# 0! = 1, 1! = 1
# 10 이상인 경우 각 자리수 를 더함
# 입력 범위 0 ~ 10000 - 0, 1, 10000 테스트 통과


count_number = int(input())

# 첫 count_number를 팩토리얼 계산을 끝내면 더이상 계산 필요 X
hash_table = [1] * 10001

for i in range(1, count_number+1):
	hash_table[i] = hash_table[i-1] * i

# 1 단계
count_number = hash_table[count_number]

while True:
	# 2 단계 [반복]
	if count_number > 9:
		# 3단계 각 자리수 더하기
		temp_num = 0
		while count_number:
			temp_num += count_number % 10
			count_number = count_number // 10
		count_number = temp_num
	else:
		print(count_number)
		break

"""
=== 구름(Goorm) '어려운 문제' 코드 리뷰 ===

[문제 이해]
- 입력된 수 N의 팩토리얼(N!)을 구하고, 그 결과값의 각 자리수를 더하는 과정을
  한 자리수가 될 때까지 반복하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성: O (문제 분석 흔적이 보임)
- 자료구조 선택: 리스트(`hash_table`)를 사용했으나, 메모리 낭비가 발생할 수 있습니다.
- 네이밍: `hash_table`이라는 변수명은 이 자료구조(리스트)의 역할과 맞지 않습니다. (해시맵이 아닙니다)

[분석 결과]
- 시간 복잡도: O(N) (팩토리얼 계산)
- 공간 복잡도: O(N) (모든 단계의 팩토리얼을 저장) -> **메모리 비효율적**
- 10000!은 매우 큰 수이므로, 이를 모두 리스트에 저장하는 것은 불필요한 메모리를 많이 사용하게 됩니다.

[힌트]
💡 메모리 최적화
- 1!부터 N!까지의 모든 값을 저장할 필요 없이, 변수 하나에 값을 누적해서 곱해나가는 방식으로도 충분합니다.
- `hash_table` 리스트를 제거하고 단일 변수로 변경해보세요.

💡 수학적 규칙 (심화)
- 팩토리얼 값들을 계산해 6! 이상을 보면 항상 9의 배수가 됩니다.
- 9의 배수의 각 자릿수를 반복해서 더하면 결과가 항상 9가 된다는 성질(디지털 루트)이 있습니다.
- 이 규칙을 활용하면, N >= 6인 경우 계산 없이 바로 9를 출력할 수 있습니다. (상수 시간 O(1) 풀이 가능)
"""