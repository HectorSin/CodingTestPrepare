# 3포함된 시각 개수 찾기
# input: N
# 00시 00분 00초부터 N시 59분 59초까지의 시간중 3이 하나라도 포함된 시간의 개수 찾기

N = int(input())

result = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            # if '3' in str(h) or '3' in str(m) or '3' in str(s):
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)