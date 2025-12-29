import sys
input = sys.stdin.readline # 입력 값이 길어질 수 있으므로 사용

# 수의 범위 20,000,000 -> O(N^2)은 피해야함
N = int(input())
# 해쉬 방식으로 접근 # 범위가 음수까지 그렇다면 
N_hash = [0] * 20000001
N_list = map(int, input().split())
for each_n in N_list:
    if each_n >= 0: # 양수면 해당 수 * 2 위치에 저장
        N_hash[each_n] += 1
    else:
        N_hash[(-1 * each_n) + 10000000] += 1

# 채크해야할 수
M = int(input())
M_list = map(int,input().split())
check_list = [] # 출력때 사용할 값
for each_m in M_list:
    if each_m >= 0:
        check_list.append(N_hash[each_m])
    else:
        check_list.append(N_hash[(each_m * (-1)) + 10000000])

# 출력
for check in check_list:
    print(check, end=" ")