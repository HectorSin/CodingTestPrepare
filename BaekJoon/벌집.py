# [백준 2292번 벌집]
# https://www.acmicpc.net/problem/2292
#
# 1. 문제 분석
# - 개요: 육각형 벌집의 중앙(1)에서 N번 방까지 가는 최소 방의 수(최단 거리)를 구하는 문제.
# - 규칙: 층(Layer)이 1씩 증가할 때마다 방의 개수가 6의 배수로 증가함.
#   - 1층: 1 (1개)
#   - 2층: 2~7 (6개)
#   - 3층: 8~19 (12개)
#   - 4층: 20~37 (18개)
# - 즉, N이 몇 번째 층에 속하는지 찾는 문제임.
#
# 2. 복잡도 분석
# - 시간 복잡도: O(√N). N=10억일 때 약 18,257번 반복하므로 제한 시간 2초 내에 충분히 통과.
# - 공간 복잡도: O(1). 변수 몇 개만 사용하므로 매우 효율적.
#
# 3. 런타임 에러(Runtime Error) 원인 분석
# - 백준에서 런타임 에러는 주로 다음과 같은 경우 발생합니다:
#   1) 입력이 없을 때 input() 호출 (로컬 실행 시 흔함) -> sys.stdin.readline 사용 권장
#   2) 0으로 나누기 (ZeroDivisionError) -> 해당 코드 없음
#   3) 인덱스 에러 (IndexError) -> 해당 코드 없음
#   4) 재귀 깊이 초과 -> 해당 코드 없음 (while문 사용)
# - 현재 코드는 로직상 문제가 없어 보입니다. 다만, 빠른 입출력을 위해 sys 모듈을 사용하는 것이 안전합니다.
#
# 4. 개선 코드 (Mathematical Approach - O(1))
# - 수열의 합 공식을 이용해 2차 방정식 근의 공식으로 한 번에 계산 가능하지만,
#   현재 while문 구현도 직관적이고 충분히 빠르므로 유지해도 좋습니다.

import sys

sys.stdin.readline

number = int(input())


def find_room(x):    
    if x == 1: return 1
    count = 1
    limit = 1
    while limit < x:
        limit += 6 * count
        count += 1
    return count

print(find_room(number))