# 숫자 카드 게임
# 문제: N x M 크기의 카드 배열에서 각 행마다 카드를 1개씩 뽑을 수 있고,
# 각 행에서 뽑은 카드 중 가장 작은 숫자가 그 행의 대표 숫자가 됨
# 모든 행의 대표 숫자 중 가장 큰 값을 찾는 문제
# 전략: 각 행의 최솟값을 구한 뒤, 그 중 최댓값을 선택 (Greedy)

# N: 행의 개수, M: 열의 개수
N, M = map(int, input().split())

# result: 각 행의 최솟값들 중 최댓값을 저장할 변수
result = 0

# N개의 행을 순회하면서 각 행의 최솟값을 확인
for i in range(N):
    # 현재 행의 M개의 숫자를 입력받아 리스트로 저장
    num_list = list(map(int, input().split()))

    # 현재 행에서 가장 작은 숫자를 찾음 (이 행의 대표 숫자)
    min_value = min(num_list)

    # 지금까지의 result와 현재 행의 최솟값을 비교하여 더 큰 값을 저장
    # 각 행의 최솟값들 중 최댓값을 갱신
    result = max(result, min_value)

# 최종 결과 출력: 모든 행의 최솟값 중 가장 큰 값
print(result)