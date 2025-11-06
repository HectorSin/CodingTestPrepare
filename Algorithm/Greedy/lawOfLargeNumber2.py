# lawOfLargeNumber.py의 해답의 경우 조건이 M이 10,000 이하이므로 해결가능하지만 만약 M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을 받음

# 입력 받기
N, M, K = map(int,input().split())
data = list(map(int,input().split()))

# 오름차순 정렬하여 가장 큰 수와 두번째로 큰 수를 찾기 위함
data.sort()

# 가장 큰 수: 배열의 마지막 요소
first_num = data[-1]
# 두번째로 큰 수: 배열의 마지막에서 두번째 요소
second_num = data[-2]

# 여기까지는 기존 방식 그대로 사용 but first_num이 몇번 사용되었는지 second_num이 몇번 사용되었는지 수를 계산해 해결 예정
count = M // (K+1) * K
count += M % (K+1)

result = 0
result += (first_num * count)
result += (second_num * (M - count))

print(result)