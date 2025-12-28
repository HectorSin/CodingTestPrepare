# 문제: 이항 계수 1 (백준 11050번)
# 링크: https://www.acmicpc.net/problem/11050
#
# [문제 분석]
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 (N K)를 구하는 문제입니다.
# 공식: C(N, K) = N! / (K! * (N-K)!)
# 입력 제한: 1 <= N <= 10, 0 <= K <= N
# 시간 제한: 1초 (N이 작아서 단순 반복문이나 재귀로도 충분합니다.)
#
# [코드 분석]
# 시간 복잡도: O(K) - 분자는 N부터 K개, 분모는 1부터 K까지 곱합니다.
# 공간 복잡도: O(1) - 상수 개의 변수만 사용합니다.
# 피드백:
# 1. 현재 로직은 이항 계수의 정의를 이용한 효율적인 구현입니다 (O(K)).
# 2. Python 3.8+ 에서는 math.comb(N, K)를 사용하면 더 간결하고 안전하게 구현할 수 있습니다.
#    예:
#    import math
#    print(math.comb(N, K))
# 
# 3. 변수명 top, bottom은 직관적이지만 numerator, denominator가 더 격식 있는 표현일 수 있습니다.
#    하지만 알고리즘 문제 풀이에서는 현재 변수명도 충분히 좋습니다.

N,K = map(int,input().split())

top = 1
bottom = 1

for i in range(K):
    top = top * (N-i)

for i in range(K):
    bottom = bottom * (i+1)

print(top//bottom)