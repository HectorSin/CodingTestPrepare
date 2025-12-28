# [Antigravity 리팩토링 피드백]
# 문제: 백준 14626 - ISBN
# 링크: https://www.acmicpc.net/problem/14626
#
# 분석 결과:
# - 목표: 13자리 ISBN 번호 중 손상된 숫자('*') 하나를 복구해야 합니다.
# - 조건: (각 자리수 * 가중치)의 합이 10으로 나누어 떨어져야 합니다. (가중치 패턴: 1, 3, 1, 3...)
# - 입력 제약: 길이는 항상 13입니다.
# - 시간 복잡도: 입력 크기가 고정되어 있어 O(1)입니다. 시간 복잡도는 문제 없습니다.
# - 논리 점검: 마지막 숫자를 계산하는 수식에 치명적인 논리적 오류가 있습니다 (가중치가 3인 경우 및 나머지 0 처리).

# ISBN 가중치
parameter = [1,3,1,3,1,3,1,3,1,3,1,3,1]

number = input()
added_parse = 0

for i in range(13):
    if number[i] == '*':
        secret_num = i
    else:
        added_parse += int(number[i]) * parameter[i]

for d in range(10):
    if (added_parse + d * parameter[secret_num]) % 10 == 0:
        print(d)
        break