"""
1로 만들기
"""

# 1s, 128mb

X = int(input()) # 1~30000
dp_table = [0] * 30001

for i in range(2,X+1):
    # 1 빼기
    case_1 = dp_table[i-1] + 1
    # 5로 나누기
    if i % 5 == 0:
        case_2 = dp_table[i//5] + 1
    else:
        case_2 = 9999
    # 3으로 나누기
    if i % 3 == 0:
        case_3 = dp_table[i//3] + 1
    else:
        case_3 = 9999
    # 2로 나누기
    if i % 2 == 0:
        case_4 = dp_table[i//2] + 1
    else:
        case_4 = 9999
    
    dp_table[i] = min(case_1,case_2,case_3,case_4)

print(dp_table[X])