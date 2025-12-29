import sys
# 문제: 백준 9012번 괄호 (https://www.acmicpc.net/problem/9012)
#
# [문제 분석]
# 1. 입력: 테스트 케이스 수 T, 그 뒤로 괄호 문자열(Length 2~50)
# 2. 조건: '('와 ')'로만 구성됨. 올바른 괄호 문자열(VPS)인지 판단.
# 3. 시간 복잡도: 제한 1초. 문자열 길이가 최대 50이므로 O(L)로 충분히 통과 가능.
#
# [코드 분석 & 피드백]
# 1. 불필요한 로직: 현재 코드는 '['와 ']'도 처리하고 있습니다. 
#    - 문제 9012번은 소괄호만 등장하므로 대괄호 관련 로직은 제거해도 됩니다.
#    - (아마도 '균형잡힌 세상' 문제(4949번)와 코드를 공유하거나 참고하신 것 같습니다)
# 2. 효율성: 스택을 이용한 O(L) 로직은 적절합니다.
# 3. 가독성: 변수명과 로직 흐름이 명확합니다.

input = sys.stdin.readline

# 공간 복잡도 O(N)
N = int(input())

for _ in range(N):
    text = input()

    # LIFO 방식
    stack = []

    # 밸런스 체크
    is_balanced = True

    # 모든 텍스트 체크
    for t in text:
        # ( [ 있으면 스택에 추가
        # 피드백: 9012번 문제에서는 '[' 체크가 필요 없습니다.
        if t == "(" or t == "[":
            stack.append(t)
        # ) 라면 스택 마지막이 ( 인지 체크
        elif t == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_balanced = False
                break
        # ] 라면 스택 마지막이 [ 인지 체크
        # 피드백: 9012번 문제에서는 이 블록(대괄호 처리)이 실행될 일이 없습니다.
        elif t == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                is_balanced = False
                break
    # 스택이 비어있는지 밸런스 되어 있는지 체크
    if not stack and is_balanced:
        print("YES")
    else:
        print("NO")