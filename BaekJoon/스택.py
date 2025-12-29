import sys
# 문제: 백준 10828번 스택 (https://www.acmicpc.net/problem/10828)
#
# [문제 분석]
# 1. 제한: 시간 0.5초 (매우 짧음) / 메모리 256MB
# 2. 입력: 명령 수 N (최대 10,000)
# 3. 시간 복잡도: N이 1만이고 시간이 0.5초이므로 O(N)으로 처리해야 합니다.
#    - Python의 경우 입출력 속도 때문에 `sys.stdin.readline` 사용이 필수적입니다.
#
# [코드 분석 & 피드백]
# 1. 런타임 에러 원인: 
#    - `sys.stdin.readline`은 입력 끝의 개행문자(\n)를 포함하여 가져옵니다.
#    - 따라서 "pop" 명령을 입력받으면 `work` 변수에는 "pop\n"이 들어갑니다.
#    - `if work == "pop":` 비교가 실패하여 `else`문(push 처리)으로 넘어갑니다.
#    - `push, number = "pop\n".split()`에서 값이 1개뿐이라 언패킹 에러(ValueError)가 발생합니다.
#    - 해결: `input().strip()`을 쓰거나 `input().split()`으로 분리하여 처리하는 것이 좋습니다.
# 2. 구조 개선: `sys.stdin.readline`을 활성화하고, 명령어 파싱 방식을 `split()`으로 통일하면 깔끔해집니다.

# 0.5초 256mb
# import sys
# input = sys.stdin.readline <- 이거 쓰니까 런타임 에러 발생 왜 그런거지?

N = int(input())

stack = []

for _ in range(N):
    work = input() # push 제외 명령어만 사용
    
    # [피드백: 개선 제안]
    # 위에서 input() 대신 sys.stdin.readline()을 사용하려면 아래와 같이 변경해보세요.
    # command = sys.stdin.readline().split()  # 공백 기준으로 분리 (개행문자도 자동 제거됨)
    # if command[0] == 'push':
    #     stack.append(command[1])
    # elif command[0] == 'pop':
    #     ... (이하 동일)
    #
    # 이렇게 split()을 쓰면 "pop\n" 문제도 해결되고, push 처리 로직도 else로 뺄 필요 없이 명확해집니다.

    if work == "pop":
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif work == "size":
        print(len(stack))
    elif work == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif work == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else: #push
        push, number = work.split()
        stack.append(int(number))