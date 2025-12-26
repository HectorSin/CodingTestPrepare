# 문제: 백준 2798번 블랙잭
# 링크: https://www.acmicpc.net/problem/2798
# 
# [문제 분석]
# - N장의 카드 중 3장을 골라 합이 M을 넘지 않으면서 M에 최대한 가까운 수를 만드는 문제입니다.
# - 입력 조건: 3 <= N <= 100, 10 <= M <= 300,000
# - N이 최대 100이므로 O(N^3) 알고리즘도 약 1,000,000 연산 내외로 1초 내에 충분히 통과합니다.
#
# [코드 분석]
# - 3중 for문을 사용한 브루트 포스(Brute Force) 방식은 이 문제의 제약 조건 하에서 정석적인 풀이입니다.
# - 시간 복잡도: O(N^3)
# - 공간 복잡도: O(N) (카드 리스트 저장)

N, M = map(int,input().split())

card_list = list(map(int,input().split()))

max_sum = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            # 3장의 카드 합 계산
            card_sum = card_list[i] + card_list[j] + card_list[k]
            
            # 합이 M을 넘지 않으면서, 그동안 찾은 최대값보다 크면 갱신
            if (card_sum > max_sum) and (card_sum <= M):
                max_sum = card_sum

print(max_sum)