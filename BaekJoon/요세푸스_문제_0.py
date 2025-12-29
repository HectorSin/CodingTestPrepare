# 문제: 백준 11866번 요세푸스 문제 0 (https://www.acmicpc.net/problem/11866)
#
# [문제 분석]
# 1. 입력: N(1~1,000), K(1~N)
# 2. 로직: 원형으로 앉은 사람들 중 K번째 사람을 계속 제거.
# 3. 시간 복잡도: 2초. N=1,000으로 작아 O(NK)나 O(N^2)도 통과 가능.
#
# [코드 분석 & 피드백]
# 1. 2025-12-29 수정 확인: K값에 따라 동적으로 회전하는 로직이 정상적으로 반영되었습니다.
#    - `check_list.rotate(-(K-1))`을 사용하여 K-1번 회전을 O(K)가 아닌 효율적인 방식으로 처리했습니다.
# 2. 성능: deque의 rotate는 효율적으로 구현되어 있어 시간 복잡도상 매우 유리합니다.
# 3. 결과: 현재 코드는 11866번 문제의 정답 코드입니다. 잘 하셨습니다!

# 2s 512mb
from collections import deque
# 1~1000

N, K = map(int,input().split())

out_list = []

check_list = deque(list(range(1,N+1))) # [1~N]

while check_list:
    # for _ in range(K-1):
    #     check_list.append(check_list.popleft()) # 가장 앞에를 빼 가장 뒤에 배치
    check_list.rotate(-(K-1)) # 연산속도 84ms -> 56ms 개선

    out_list.append(check_list.popleft())

print("<",end="")
print(*out_list,sep=", ",end="")
print(">",end="")