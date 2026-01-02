# 문제 분석: 피보나치 함수 (백준 1003번) - https://www.acmicpc.net/problem/1003
# 현재 접근: 재귀 함수를 이용한 단순 시뮬레이션
# 힌트 레벨 1: 시간 제한이 0.25초로 매우 짧습니다. N=40일 때 재귀 호출이 몇 번 일어날지 2^N과 비교해보세요.
# 힌트 레벨 2: 중복 계산을 막기 위해 이미 계산한 값은 저장해두는 방법(Memoization)이나, 작은 수부터 올라가는 DP를 고려해보세요.
# 시간이 매우 짧다 (0.25초)

import sys
input = sys.stdin.readline

fibo_table = [[-1,-1] for _ in range(41)]
fibo_table[0], fibo_table[1] = [1,0],[0,1]

def fibonacci(number):
    if fibo_table[number] == [-1,-1]:
        for i in range(number+1): 
             if fibo_table[i] == [-1,-1]:
                fibo_table[i] = [fibo_table[i-1][0] + fibo_table[i-2][0], fibo_table[i-1][1] + fibo_table[i-2][1]]
        return fibo_table[number]
    else:
        return fibo_table[number]


T = int(input())

for i in range(T):
    N = int(input())
    fibo_result = fibonacci(N)
    print(fibo_result[0], fibo_result[1])

