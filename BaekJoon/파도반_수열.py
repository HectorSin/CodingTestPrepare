import sys
input=sys.stdin.readline

T = int(input())

dp_table = [0] * 101
dp_table[1],dp_table[2],dp_table[3],dp_table[4],dp_table[5] = 1,1,1,2,2


for _ in range(T):
    N = int(input())

    if N >= 5:
        for i in range(6,N+1):
            if dp_table[i] != 0:
                pass
            else:
                dp_table[i] = dp_table[i-1] + dp_table[i-5]

    print(dp_table[N])
