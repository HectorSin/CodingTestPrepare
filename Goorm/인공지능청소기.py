# https://level.goorm.io/exam/43068/1a-%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5-%EC%B2%AD%EC%86%8C%EA%B8%B0/quiz/1
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# DFS방식? DP 방식?

def check_route(x,y,n):
	"""
	좌표 0,0에서 n초의 시간만큼 움직여 x,y에 도착 가능한지 체크하는 함수
	1. 최소 거리 계산 [시간(n)이 최소 거리보다 작다면 바로 실패]
	2. 최소 거리 + 짝수 <- 기존 구간에서 왔다 갔다하며 시간을 버려야 하기에
	"""
	short_time = abs(x) + abs(y)

	if n < short_time:
		print("NO")
	else:
		if (n - short_time) % 2 == 0:
			print("YES")
		else:
			print("NO")



N = int(input())

for _ in range(N):
	X,Y,N = map(int,input().split())
	check_route(X,Y,N)

"""
=== 구름(Goorm) 인공지능 청소기 코드 리뷰 ===

[문제 이해]
- (0, 0)에서 시작하여 정확히 N초 뒤에 (X, Y)에 도달할 수 있는지 판별하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O (docstring 및 상단 주석)
- 문제 분석 단계: 수학적 규칙(최단 거리 + 짝수 시간 차이)을 잘 파악했습니다. DFS/DP 같은 복잡한 탐색보다 효율적인 O(1) 방식을 선택한 점이 훌륭합니다.
- 자료구조 선택 근거: 특별한 자료구조 없이 수식으로 해결하여 최적입니다.
- 알고리즘 설계: 구체적이며 구현과 일치합니다.

[현재 접근 방식]
- 맨해튼 거리(Manhattan Distance)를 구하고, 남은 시간의 홀짝(Parity) 여부를 체크하는 방식

[분석 결과]
- 시간 복잡도: O(T) (테스트 케이스 수만큼 반복, 각 연산은 O(1))
- 예상 결과: 통과 (매우 효율적임)

[힌트]
💡 아주 잘 해결하셨습니다!
- 복잡한 탐색 알고리즘에 빠지지 않고 문제의 핵심(거리와 시간의 홀짝성)을 잘 짚어내셨습니다.
- 변수 이름 `N`이 테스트 케이스 수와 입력 시간 변수로 중복 사용되고 있습니다. 테스트 케이스 수는 `T` 등의 다른 이름으로 하는 것이 가독성에 좋습니다.
- 입력이 매우 많을 경우를 대비해 `sys.stdin.readline`을 사용하는 습관을 들이면 좋습니다.

[더 알아보면 좋을 것]
- 맨해튼 거리(Manhattan Distance) vs 유클리드 거리(Euclidean Distance)
- Parity(홀짝성)을 이용한 grid 문제 유형
"""