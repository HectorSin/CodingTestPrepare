"""
효율적인 화폐 구성
"""

N,M = map(int,input().split())

money_list = []
for _ in range(N):
    money_list.append(int(input()))

dp_table = [0] * (M+1)

for i in money_list:
    if i <= M:
        dp_table[i] = 1

for j in range(1,M+1):
    for money in money_list:
        if j-money >= 0 and dp_table[j-money] != 0:
            if dp_table[j] == 0:
                dp_table[j] = dp_table[j-money] + 1
            else:
                dp_table[j] = min(dp_table[j], dp_table[j-money] + 1)

if dp_table[M] == 0:
    print(-1)
else:
    print(dp_table[M])