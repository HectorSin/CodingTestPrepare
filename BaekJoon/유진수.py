# string = "12361432"

# leter_len  =len(string)

# for i in range(1,leter_len):
#     first_letter = string[0:i+1]
#     second_letter = string[i:leter_len-1]

# fir_num = 1
# for word in first_letter:
#     fir_num = fir_num * int(word)

# sec_num =1
# for word in second_letter:
#     sec_num = sec_num * int(word)

# if fir_num == sec_num:
#     print("YES")
# else:
#     print("NO")


"""
# 문제 분석: 1356번 유진수
# https://www.acmicpc.net/problem/1356
#
# 문제 개요:
#   어떤 수 N을 두 부분으로 나누었을 때, 앞부분의 자리수 곱과 뒷부분의 자리수 곱이
#   같아지는 경우가 있는지 확인하는 문제입니다.
#
# 시간 복잡도 분석:
#   입력 N은 최대 2,147,483,647로 길이는 최대 10자리입니다.
#   현재 코드는 분할 위치를 옮겨가며 계산하므로 O(L^2) (L:자릿수) 복잡도를 가집니다.
#   L=10이므로 연산 횟수는 매우 적어(약 100회) 시간 내에 넉넉히 통과합니다.
#
# 피드백:
#   - 입력 크기가 작아서 현재 접근 방식(Deque 사용)도 문제 해결에 충분합니다.
#   - 파이썬의 문자열 슬라이싱을 활용하면 코드를 더 간결하게 작성할 수 있습니다.
"""

from collections import deque

text = input()

text_list = []
for t in text:
    text_list.append(int(t))

text_que = deque(text_list)
# 💡 힌트 Level 1: 문자열은 슬라이싱(text[:i], text[i:])이 가능하므로
# 굳이 리스트나 Deque로 변환하지 않아도 풀 수 있습니다.

# 저장할 큐 2개로 나눠
# first_que = deque()
first_num = 1

if len(text_que) == 1:
    print("NO")
else:
    checker = False

    for _ in range(len(text)-1):
        first_num = first_num * text_que.popleft()

        second_num = 1
        for i in text_que:
            second_num = i * second_num
        
        # 🤔 생각해보기: 지금은 뒷부분 곱을 매번 새로 구하고 있습니다(O(L^2)).
        # 전체 곱을 미리 구해두고(0이 없는 경우), 앞부분 곱으로 나누면 O(L)로 줄일 수 있을까요?
        # (0이 포함된 경우는 주의가 필요합니다)

        # 만약에 첫놈이 뒷놈이랑 같으면 
        if first_num == second_num:
            print("YES")
            checker = True
            break
    if not checker:
        print("NO")