import sys

# 입력 [0.1ms 환경에서 습관화]
input = sys.stdin.readline

N = int(input())
sizes = list(map(int,input().split()))
T, P = map(int,input().split())

# print(sum(math.ceil(s / T) for s in sizes))
print(sum((s+T-1)//T for s in sizes))
print((N//P), (N%P))