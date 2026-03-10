"""
결국은 길찾기 문제
알고리즘으로 BFS를 사용해서 진행하는 게 맞는 것으로 보입니다. 
지나왔던 장소를 저장하고 갈 수 있는 곳은 오른쪽, 왼쪽, 위, 아래, 총 네 가지 방향입니다. 
모든 칸에서 BFS를 실행해야 되는데.
여기서 사실 위치를 기억한다기보다, 가장 큰 숫자만 기억하면 됨
경우의 수는 4*3*3=36
1. 큐에 시작하는 위치 저장.
2. 다음 위치 계산.
3. 해당 위치가 범위에 벗어나는지 체크.

여기서는 사 곱하기 삼 곱하기 삼 법칙만 따르면, 방문했던 위치를 다시 방문할 수가 없기 때문에 해당 가능성은 제외됩니다. 
"""

# import sys
# input = sys.stdin.readline
# from collections import deque

# N, M = map(int,input().split())

# graph = []

# for _ in range(N):
#     graph.append(list(map(int,input().split())))

# def check_loc(i,j):
#     """
#     해당 좌표가 다음 조건에 벗어나는지 체크
#     """
#     if i < 0 or i >= N or j < 0 or j >= M:
#         return False
#     return True
    

# def BFS(i,j):
#     """
#     길찾기 알고리즘
#     """
#     global graph
    
#     next_x = [1,0,-1,0]
#     next_y = [0,-1,0,1]
    
#     max_BFS = 0
    
#     for a in range(4):
#         for b in range(3,6):
#             for c in range(3,6):
#                 current_num = graph[i][j]
                
#                 next_i = i + next_x[a]
#                 next_j = j + next_y[a]
                
#                 if check_loc(next_i,next_j):
#                     current_num += graph[next_i][next_j]
#                 else:continue
                    
#                 next_i = i + next_x[(a+b)%4]
#                 next_j = j + next_y[(a+b)%4]
                
#                 if check_loc(next_i,next_j):
#                     current_num += graph[next_i][next_j]
#                 else:continue
                
#                 next_i += next_x[(((a+b)%4)+c)%4]
#                 next_j += next_y[(((a+b)%4)+c)%4]
                
#                 if check_loc(next_i,next_j):
#                     current_num += graph[next_i][next_j]
#                     max_BFS = max(max_BFS, current_num)
#                 else:continue
    
#     return max_BFS
    
    

# max_num = 0

# for i in range(N):
#     for j in range(M):
#         max_num = max(max_num, BFS(i,j))
    
# print(max_num)

"""
=== 백준 14500번 코드 리뷰 ===

[문제 이해]
- N×M 격자에 테트로미노(4칸 도형) 하나를 놓아 덮이는 숫자 합의 최댓값을 구하는 문제입니다
- 테트로미노 5종류 × 회전/반사 포함 총 19가지 배치 형태가 존재합니다

[설계 프로세스 평가]
- 주석 작성 여부: O
- 문제 분석 단계: 보완 필요
- 자료구조 선택 근거: 불명확 (BFS라고 명시했지만 실제 구현과 다름)
- 알고리즘 설계: 추상적
- 설계-구현 일치도: 부분 불일치

[현재 접근 방식]
- 4방향 * 3가지 보조 방향 조합으로 4칸을 탐색하려는 아이디어
- for a, b, c 3중 루프를 사용했지만 실제 BFS는 사용하지 않음

[분석 결과]
- 시간 복잡도: O(N * M * 36) - 중복 계산 포함
- 예상 결과: 틀림 (Wrong Answer)

[발견된 버그 2가지]
🐛 Bug 1: c 변수가 선언되었지만 전혀 사용되지 않습니다
  - range(3,6)으로 3회 반복하지만 c는 어디에도 쓰이지 않음
  - 불필요하게 9배의 연산이 수행됨

🐛 Bug 2: 세 번째로 방문하는 칸(65~70번째 줄)이 첫 번째 칸(51~56번째 줄)과 동일한 위치를 사용합니다
  - 즉, 시작점 → 방향 a → 방향 (a+b)%4 → 방향 a (중복!) 순서로 탐색
  - 4칸이 아니라 사실상 3칸만 유효하며, 마지막 칸은 두 번째와 같은 곳

[힌트]
💡 두 가지를 생각해보세요:

1. 테트로미노 모양을 어떻게 분류할 수 있을까요?
   - I, O, S/Z, L/J 형태는 DFS로 한 방향씩 뻗어나가는 방식으로 구현 가능합니다
   - 단, T형만은 DFS로 자연스럽게 나오지 않는 특수한 모양입니다
   - T형을 어떻게 별도로 처리할지 고민해보세요

2. DFS로 4칸을 탐색할 때, 방문 여부를 어떻게 관리해야 할까요?

[설계 개선 제안]
알고리즘을 다음 구조로 재설계해보세요:
  1. 모든 시작점 (i, j)에서 DFS로 4칸 연결된 최대 합 탐색
  2. T자형은 DFS로 만들기 어려우므로 → 한 점에서 상하좌우 3방향 선택 조합으로 별도 처리

[더 알아보면 좋을 것]
- DFS + 백트래킹으로 4칸 연결 탐색하는 패턴
- T자형 테트로미노의 특수성 (왜 DFS로 처리하기 까다로운가?)
- 테트로미노 19가지 형태를 좌표 offset으로 하드코딩하는 접근법도 있습니다
"""

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int,input().split())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

visited = [[False] * M for _ in range(N)]

def check_loc(i,j):
    """
    해당 좌표가 다음 조건에 벗어나는지 체크
    """
    if i < 0 or i >= N or j < 0 or j >= M:
        return False
    return True
    
def DFS(i,j,depth,current_sum):
    """
    depth: 깊이
    current_sum: 숫자 합
    """
    global max_num
    
    if depth == 4:
        max_num = max(current_sum, max_num)
        return
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    for d in range(4):
        ni, nj = i+dx[d], j+dy[d]
    
        if check_loc(ni,nj) and not visited[ni][nj]:
            visited[ni][nj] = True
            DFS(ni,nj,depth+1,current_sum+graph[ni][nj])
            visited[ni][nj] = False

def t_form(i,j,current_num):
    global max_num
    
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    
    for d in range(4):
        i1, j1 = i+dx[(d+1)%4], j+dy[(d+1)%4]
        i2, j2 = i+dx[(d+2)%4], j+dy[(d+2)%4]
        i3, j3 = i+dx[(d+3)%4], j+dy[(d+3)%4]
        
        if check_loc(i1,j1) and check_loc(i2,j2) and check_loc(i3,j3):
            max_num = max(max_num, current_num + graph[i1][j1] + graph[i2][j2] + graph[i3][j3])
        
        continue
    

max_num = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        DFS(i,j,1,graph[i][j])
        visited[i][j] = False
        t_form(i,j,graph[i][j])
    
print(max_num)

"""
=== 백준 14500번 코드 리뷰 (2차) ===

[설계 프로세스 평가]
- 주석 작성 여부: O (1차보다 개선됨)
- 문제 분석 단계: 보완 필요
- 자료구조 선택 근거: 보통 (DFS + visited 선택은 적절)
- 알고리즘 설계: 보통
- 설계-구현 일치도: 부분 불일치 (t_form에 버그 존재)

[현재 접근 방식]
- DFS + 백트래킹으로 4칸 연결 탐색
- T자형은 t_form 함수로 별도 처리 (아이디어는 정확함!)

[분석 결과]
- 시간 복잡도: O(N × M × 4^4) → 실질적으로 O(N × M × 12) 수준
- DFS 부분: ✅ 정확
- t_form 부분: ❌ 버그 있음 → 틀림 예상

[DFS 함수 평가]
✅ 훌륭합니다! 아이디어와 구현이 모두 정확합니다
- visited 배열로 중복 방문 방지
- depth == 4에서 max 갱신
- 백트래킹(visited = False)도 정확

[t_form 함수의 버그]
🐛 Bug 1: 186~190번째 줄 - 4방향 중 하나라도 범위를 벗어나면 return합니다
  - 격자 모서리/가장자리에 있는 칸은 T형 체크 자체가 불가능해집니다
  - "4방향 합산"과 "하나 제외"를 분리해서 생각해보세요

🐛 Bug 2: 193~195번째 줄 - for 루프 변수 이름이 minus인데 실제로는 d를 사용합니다
  - 193번 줄: for minus in range(4)
  - 194번 줄: i+dx[d], j+dy[d] ← d는 마지막 루프의 값(3)으로 고정됨!
  - minus를 사용해야 4방향을 각각 제외할 수 있습니다

[힌트]
💡 t_form 로직을 다음 두 단계로 나눠 생각해보세요:
  1. 4방향을 각각 독립적으로 체크 (범위 밖이면 '그냥 건너뛰기')
  2. 유효한 방향들의 합을 먼저 구한 뒤, 각 방향을 하나씩 빼서 최댓값 갱신

[더 알아보면 좋을 것]
- 루프 변수 이름과 사용 변수가 일치하는지 항상 확인하는 습관
- 경계 조건(edge case)에서 함수가 조기 종료되지 않도록 주의
"""
