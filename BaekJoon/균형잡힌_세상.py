# [백준 4949번: 균형잡힌 세상](https://www.acmicpc.net/problem/4949)
#
# [문제 분석]
# 1. 문제 개요: 소괄호 '()'와 대괄호 '[]'가 올바르게 짝을 이루는지 확인하는 문제입니다.
# 2. 주의할 점: 
#    - 단순 개수 카운팅으로는 풀 수 없습니다.
#    - 예: "([)]" -> 소괄호, 대괄호 개수는 각각 1개로 같지만, 짝이 맞지 않아 "no"여야 합니다.
#    - **가장 최근에 열린 괄호가 가장 먼저 닫혀야 한다**는 특성(LIFO) 때문에 **스택(Stack)** 자료구조가 필요합니다.
# 3. 입력 종료 조건: 온점 하나 "."가 들어오면 종료합니다.
# 4. 성능: 문자열 길이는 최대 100글자이므로, O(N) 복잡도인 스택을 사용하면 시간 초과는 전혀 걱정하지 않으셔도 됩니다.
#
# [개선 방안]
# - 리스트를 스택처럼 활용하세요 (`append()`, `pop()`).
# - 열린 괄호 '(', '['는 스택에 넣습니다.
# - 닫힌 괄호 ')', ']'가 나오면:
#   1. 스택이 비어있는지 확인 (비어있으면 "no")
#   2. 스택의 top(마지막 요소)이 짝이 맞는 괄호인지 확인 (맞으면 pop, 아니면 "no")
# - 모든 문자열을 처리한 후, 스택이 비어 있어야 "yes"입니다.

"""
[기존 코드 피드백]
Q: 간단하게 만들었는데 이것도 시간 초과 예상 큐로 만들어야 한가?
A: 
1. **시간 초과 여부**: 문자열 길이가 최대 100이라서 시간 복잡도는 문제되지 않습니다. 현재 방식도 빠릅니다.
2. **논리적 오류 (Critical)**: **큐가 아니라 '스택'을 써야 합니다.**
   - 작성하신 코드는 단순히 개수만 세고 있습니다 (`count_1`, `count_2`).
   - 반례: "([)]" 
     - 작성하신 코드: '(' 카운트증가 -> '[' 카운트증가 -> ')' 카운트감소(성공) -> ']' 카운트감소(성공) ==> 결과 "yes" (오답)
     - 정답: "no"
   - 괄호의 **순서**가 중요하므로 스택을 사용해야만 풀 수 있습니다.

[스택을 활용한 올바른 로직 제안]
"""

# while True:
#     text = input().rstrip() # 개행 문자 제거
#     if text == ".":
#         break
    
#     stack = []
#     is_balanced = True
    
#     for t in text:
#         if t == "(" or t == "[":
#             stack.append(t)
#         elif t == ")":
#             if stack and stack[-1] == "(":
#                 stack.pop()
#             else:
#                 is_balanced = False
#                 break
#         elif t == "]":
#             if stack and stack[-1] == "[":
#                 stack.pop()
#             else:
#                 is_balanced = False
#                 break
    
#     if is_balanced and not stack: # 짝이 다 맞고 스택도 비어있어야 함
#         print("yes")
#     else:
#         print("no")


import sys
input = sys.stdin.readline

# 반복
while True:
    text = input().rstrip()
    # 끝인지 확인
    if text == ".":
        break
    # 중간에 종료되었을때 체크용도
    even_checker = True
    stack = []
    # 모든 텍스트 확인
    for each_text in text:
        # ( [ 인자라면 스택에 넣음
        if each_text == "(" or each_text == "[":
            stack.append(each_text)
        elif each_text == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                even_checker = False
                break
        elif each_text == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                even_checker = False
                break
    
    # 스택이 비어있는지 체크 & 체커 확인
    if even_checker and not stack:
        print("yes")
    else:
        print("no")