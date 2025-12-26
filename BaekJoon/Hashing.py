# 문제: 백준 15829번 Hashing
# 링크: https://www.acmicpc.net/problem/15829
# 
# [문제 분석]
# - APC(Ansan Pseduo Code)의 해싱 함수를 구현하는 문제입니다.
# - 수식: H = Σ(a_i * r^i) mod M
#   (r = 31, M = 1234567891)
# - 입력: 문자열 길이 L (1 ≤ L ≤ 50), 문자열 (소문자)
#
# [코드 분석]
# - 현재 코드는 반복문 내에서 모듈러 연산을 활용하여 거듭제곱을 효율적으로 처리하고 있습니다.
# - r_power를 매번 31씩 곱하고 mod M을 수행하므로, O(L) 시간 복잡도로 매우 효율적입니다.
# - 정수 오버플로우 걱정 없이 안정적으로 동작하는 훌륭한 코드입니다.

L = int(input())
text = input()

r_power = 1
output = 0

for alph in text:
    output += ((ord(alph)-ord('a')+1) * (r_power))
    r_power = (31 * r_power) % 1234567891

print(output % 1234567891)