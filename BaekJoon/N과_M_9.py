"""
작은 숫자부터 시작하는 주어진 숫자 조합 만들기 함수

DFS 방식 & 재귀함수 사용해서 해결해볼까 함
"""

# N, M = map(int,input().split())

# num_list = list(map(int,input().split()))
# num_list.sort()

# def DFS(depth):
#     """
#     """
#     global visited_list, last_num, used_list
    
#     if depth == M:
#         print(*visited_list)
#         return
    
#     for i in range(N):
#         if num_list[i] != last_num and i not in used_list:
#             visited_list.append(num_list[i])
#             used_list.append(i)
#             DFS(depth+1)
#             visited_list.pop()
#             used_list.pop()
#             last_num = num_list[i]


# visited_list = []
# used_list = []
# last_num = 0

# DFS(0)

"""
=== 백준 15663번 코드 리뷰 ===

[문제 이해]
- 이 문제는 N개의 자연수 중에서 M개를 고르는 순열을 구하되, 중복되는 수열은 제외하고 사전 순으로 배열하는 문제입니다.

[설계 프로세스 평가]
- 주석 작성 여부: O (그러나 단편적임)
- 문제 분석 단계: 보완 필요
- 자료구조 선택 근거: 없음
- 알고리즘 설계: 추상적
- 설계-구현 일치도: 일치

[현재 접근 방식]
- DFS를 기반으로 한 백트래킹으로 수열의 자리를 채우고 있습니다.
- 특정 깊이(depth)에서 똑같은 숫자를 중복 탐색하지 않기 위해 `last_num` 변수를 두고 필터링합니다.

[분석 결과]
- 시간 복잡도: O(N!) 미만
- 예상 결과: 틀림
- 원인: `last_num`이 전역(global) 변수로 선언되어 있어 논리적 오류가 발생합니다. 깊은 탐색 후 되돌아왔을 때, 이전 깊이에서 갱신되었던 `last_num`이 그대로 유지되면서 앞으로 출력해야 할 정상적인 경우의 수까지 건너뛰게(skip) 만듭니다.

[힌트]
💡 `last_num`의 유효 범위(Scope)를 변경해보세요!
- 입력이 '1 7 9 9 / M=2' 일 때, 현재 코드는 '7 1'을 출력해야 함에도 건너뜁니다. 이전 과정에서 방문했던 `last_num = 1` 때문에 필터링되기 때문입니다.
- 중복된 수열 방지를 위해 필요한 "직전에 고른 숫자"는 '현재 자리(같은 depth)' 단위로만 독립적으로 기억되어야 합니다.
- `last_num`을 `global`로 관리하지 않고, `DFS` 함수 내부에서 초기화되는 지역(local) 변수로 변경해 보세요!

[설계 개선 제안]
- 다음 구조로 주석을 작성하며 설계하는 습관을 들여보세요:
  1. 문제 핵심 파악: 순열 생성, 그리고 중복 수열 필터링
  2. 필요한 자료구조 선택: 방문 검사를 위한 배열 (O(1))
  3. 알고리즘 단계별 설명: 지역 변수와 전역 변수의 역할 구분
  4. 시간/공간 복잡도 예측

[더 알아보면 좋을 것]
- 리스트 내부 탐색인 `i not in used_list`는 O(N)의 시간이 걸립니다. N이 작아서 통과할 순 있지만, 방문 처리를 위해 `used = [False] * N` 형태의 Boolean 배열을 사용하여 O(1) 시간에 확인하는 것이 정석적인 백트래킹 팁입니다!
"""

N, M = map(int,input().split())

num_list = list(map(int,input().split()))
num_list.sort()

def DFS(depth):
    """
    """
    global visited_list, used_list
    
    if depth == M:
        print(*visited_list)
        return
    
    last_num = 10000
    
    for i in range(N):
        if used_list[i] == 0:
            if num_list[i] != last_num:
                visited_list.append(num_list[i])
                used_list[i] = 1
                DFS(depth+1)
                visited_list.pop()
                used_list[i] = 0
                last_num = num_list[i]


visited_list = []
used_list = [0] * (N+1)

DFS(0)

"""
=== 백준 15663번 2차 코드 리뷰 ===

[문제 이해]
- 이전 피드백을 반영하여 N개의 자연수 중에서 M개를 고르며 중복을 제외하고 순열을 구하는 코드를 작성하고 계십니다.

[설계 프로세스 평가]
- 주석 작성 여부: X
- 문제 분석 단계: 없음 (이번에는 피드백 반영 및 구현 위주로 진행하셨네요!)

[현재 접근 방식]
- `last_num`을 `DFS` 함수 내부의 지역 변수로 훌륭하게 변경하셨습니다! 👏
- `used_list`를 O(N)이 걸리던 탐색에서 인덱스로 접근하여 O(1)에 확인할 수 있는 정수 배열로 성공적으로 개선하셨습니다!

[분석 결과]
- 시간 복잡도: O(N!) 이하 
- 예상 결과: 틀림 (특정 케이스에서 아무것도 출력되지 않을 수 있습니다)
- 원인: `last_num`의 초기값 설정

[힌트]
💡 `last_num`의 초기값을 확인해 보세요!
- 현재 DFS 시작 시 `last_num = 9`로 초기화되어 있습니다. 
- 만약 입력으로 주어지는 수열에 `9`가 있다면 어떻게 될까요? (예: `4 2`, `9 9 9 9` 입력)
- 반복문에서 처음 마주하는 숫자가 `9`라면, 처음부터 `if num_list[i] != last_num:` 조건에 걸려 아예 선택되지 않고 넘어가게 됩니다!
- 문제의 조건에서 주어지는 숫자는 최소 1 이상의 자연수이므로, 수열에 **절대 등장할 수 없는 수**(예를 들어 `0`이나 `-1`)로 초기화해 보세요.

[더 알아보면 좋을 것]
- `used_list` 배열의 크기를 `[0] * (N+1)`로 하셨는데, 파이썬 인덱스는 0부터 시작하고 반복문이 `range(N)`이므로 `[0] * N`으로 만들어도 모든 요소에 접근하기 충분합니다!
"""