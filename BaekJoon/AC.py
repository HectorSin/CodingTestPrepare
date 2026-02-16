# 1s, 256MB

# T 최대 100
# p 1~100,000
# n 0~100,000

# 함수 -> input 개수 -> 배열 체크 이 과정을 함수로 다루고 T회 반복
# 사실 deque를 사용하면 정렬없이 앞 뒤만 찾으면 되기에 사용

from collections import deque
import sys
input = sys.stdin.readline

def ad_func():
    ad = input().rstrip()

    P = int(input())

    check = input().rstrip()

    if P == 0:
        check_list = []
    else:
        check_list = deque(check[1:-1].split(','))
    
    dir = 1

    for f in ad:
        if f == 'R':
            dir = dir * (-1)
        elif f == 'D':
            if dir == 1 and check_list:
                check_list.popleft()
            elif dir == -1 and check_list:
                check_list.pop()
            else:
                return 'error'
    
    check_list = list(check_list)

    if dir != 1:
        check_list = check_list[::-1]

    return "[" + ",".join(check_list) + "]"
    

T = int(input())

for _ in range(T):
    print(ad_func())
