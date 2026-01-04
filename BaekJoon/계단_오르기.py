# 1s, 128mb
# 문제 분석: 백준 2579번 '계단 오르기' (https://www.acmicpc.net/problem/2579)
# 현재 접근: DP 사용 시도, 하지만 인덱스와 점화식 구성에 혼동이 있음. N=1일 때 에러 발생 가능.
# 힌트 레벨 1 (엣지 케이스): N이 1일 때 step_hash[2]를 조회하면 IndexError가 발생합니다. 예외 처리가 필요합니다.
# 힌트 레벨 2 (인덱스 매칭): step_list는 0-index, step_hash는 1-index입니다. i번째 계단의 점수는 step_list[i-1]임에 유의하세요.
# 힌트 레벨 3 (점화식 수정):
#   계단 i에 도착하는 방법은 두 가지입니다.
#   1. (i-2) -> i
#   2. (i-3) -> (i-1) -> i
#   이 두 경우에 맞춰 올바른 점수(step_list[...])를 더하고 있는지 확인해보세요. 현재 코드는 인덱스가 조금 엇갈려 있습니다.
import sys
input = sys.stdin.readline

n = int(input()) # 300이하

step_list = []

for _ in range(n):
    step_list.append(int(input()))

step_hash = [0] * (n+1)
step_hash[1] = step_list[0]
if n > 1:
    step_hash[2] = step_hash[1] + step_list[1]

for i in range(3,n+1):    
    step_hash[i] = max(step_hash[i-2]+step_list[i-1],step_hash[i-3]+step_list[i-2]+step_list[i-1])

print(step_hash[n])

