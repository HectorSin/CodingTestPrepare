"""
DSLR 문제
D - 더블 [두배]
S - -1
L - 왼쪽으로 이동
R - 오른쪽으로 이동

이 경우 어떤 알고리즘으로 접근해야 하는가?

여기서 +1은 없고 -1만 있다는 점
x2 를 하더라도 10000 이하는 없앤다는 점
DP 방식으로 해결해야 하는가?

DS만 있었다면 목표 숫자보다 크게 만든 다음 마이너스만 진행
각 자릿수를 빼기 위해서는 L, R을 하여 1의 자리로 옮긴 다음 빼기 진행
두배를 하게 되면 이게 알고리즘적으로 어떻게 알 수 있지?
계속 두배를 하면서 각 자릴수의 일치 수가 3개 이상일때까지 반복?
순서가 다른 경우엔?
1234 1243의 경우?
빼기만 되니 차라리 두배를 계속 진행하며 모든 수가 각 자릿수보다 크게 될때까지 반복?
맞아 결국 빼기와 위치 이동만 되고 L또는 R을 4번 반복해서 각 자릿수가 크게 될때까지만 반복

1. while문 [각 자릿수가 목표수보다 커질때까지 2배 & L 4번]
2. 가장 각 자릿수 차이가 낮은 L기억
3. 각 자릿수를 S로 빼기
4. 다 뺀후 원래 위치로 L or R
"""

# import sys
# input = sys.stdin.readline

# T = int(input())

# def clear_list(check_list):
#     """
#     1이 들어올 경우 [1,0,0,0] -> [0,0,0,1] 형태로 정리하는 함수
#     """
#     for _ in range(3):
#         if check_list[-1] == -1:
#             check_list = right_shift(check_list)
#         else:
#             break
    
#     for i in range(4):
#         if check_list[i] == -1:
#             check_list[i] = 0
    
#     return check_list
            
# def left_shift(move_list):
#     """
#     list 왼쪽 이동
#     """
#     return [move_list[1],move_list[2],move_list[3],move_list[0]]

# def right_shift(move_list):
#     """
#     list 오른쪽 이동
#     """
#     return [move_list[3],move_list[0],move_list[1],move_list[2]]

# def check_all(check_list, target_list):
#     """
#     각 자릿수를 이동해보면서 전부 목표수보다 커지는지 체크
#     """
#     current_check = check_list
    
#     for _ in range(4):
#         current_check = left_shift(current_check)
#         checker = True
#         for i in range(4):
#             if current_check[i] < target_list[i]:
#                 checker = False
#         if checker:
#             return True
#     return False

# def double_shift(target_list):
#     new_list = [0,0,0,0]
#     for i in [3,2,1,0]:
#         new_list[i] += (target_list[i] * 2)
#         if new_list[i] >= 10:
#             if i != 0:
#                 new_list[i-1] += 1
#             new_list[i] -= 10
#     return new_list

# def check_shortest_way(target_list):
#     """
#     LRS를 적절히 조합해 가장 적은 방식으로 원하는 타겟에 접근하는 방법 return
#     1. seed를 0~4로 제공
#     2. 각 seed를 더한 인덱스가 target_number라고 생각
#     3. target보다 적은 수만큼 S추가
#     4. L 또는 R 추가
#     """
    
    
    
    

# for _ in range(T):
#     A, B = input().split()
#     A_list = [-1,-1,-1,-1]
#     B_list = [-1,-1,-1,-1]
    
#     control_list = ""
    
#     for idx,a in enumerate(A):
#         A_list[idx] = int(a)
#     for idx,b in enumerate(B):
#         B_list[idx] = int(b)
#     A_list = clear_list(A_list)
#     B_list = clear_list(B_list)
    
#     while not check_all(A_list,B_list):
#         # 반복
#         A_list = double_shift(A_list)
#         control_list += "D"
    
#     # 이제 돌면서 가장 작은 수의 빼기 방식 구하기
    
#     control_list += check_shortest_way(A_list)
    
#     print(control_list)
    

"""
=== 백준 9019번 코드 리뷰 ===

[문제 이해]
- 이 문제는 주어진 정수 A를 B로 변환하기 위한 최소한의 명령어(D, S, L, R) 나열을 구하는 문제입니다. 

[설계 프로세스 평가]
- 주석 작성 여부: O
- 문제 분석 단계: 보완 필요 (최소 횟수를 찾는 문제의 특성을 탐색 관점으로 볼 필요가 있습니다)
- 자료구조 선택 근거: 없음
- 알고리즘 설계: 구체적 (하지만 최단 경로 탐색이 아닌 규칙성/시뮬레이션 기반 접근)
- 설계-구현 일치도: 일치 (고민한 논리를 바탕으로 구현을 시도 중)

[현재 접근 방식]
- 숫자를 각 자릿수의 리스트로 변환하고, 조건문을 통해 각 자릿수에 맞게 시프트와 2배, 빼기 연산을 단계적으로 맞춰가려는 시뮬레이션 방식입니다.

[분석 결과]
- 시간 복잡도: 파악 불가 (상태 공간을 체계적으로 탐색하지 않아 최단 거리를 보장할 수 없으며 무한 루프 위험이 있음)
- 예상 결과: 틀림 또는 시간 초과

[힌트]
💡 가중치가 같은 상황에서 "최소한의 연산(최단 경로)"을 구해야 하는 문제입니다.
- 상태(숫자 0~9999)를 노드로, 4가지 연산(D, S, L, R)을 간선으로 생각해보세요.
- 어떤 알고리즘이 최단 거리를 보장할 수 있을까요?
- [추가 팁] 숫자를 배열로 분리해 매번 합치는 방식보다 정수형 상태에서 몫(//)과 나머지(%) 연산만으로 D, S, L, R 결과를 O(1)에 계산하는 것을 추천합니다.

[설계 개선 제안]
코드 작성 전 다음 관점에서 고민을 주석으로 남겨보시면 훨씬 체계적인 설계가 가능합니다:
1. 문제의 핵심 파악: "최소 명령 횟수 찾기" -> 최단 경로 탐색 알고리즘 적용
2. 상태 공간의 파악: 숫자 범위(0 ~ 9,999)가 노드의 총 개수가 됨.
3. 자료구조 선택: 각 노드의 탐색 순서를 보장할 구조(Queue), 이미 방문한 숫자를 기록할 배열(visited)
4. 결과 역추적: 어떤 연산을 통해 해당 숫자에 도달했는지 경로를 기록하는 방법

[더 알아보면 좋을 것]
- 너비 우선 탐색(BFS) 패턴
- BFS에서 어떤 경로(명령어)로 현재 노드에 도달했는지 추적/저장하는 방법
"""

"""
알고리즘을 설계해서 이를 해결할려고 접근했지만
생각보다 중간중간 벗어나는 예외구간이 많았고 테스트 케이스에 맞게 구현을 하더라도 정답이 아닐거라고 판단
힌트를 확인해보니 BFS방식으로 접근하는 방식
"""

# import sys
# input = sys.stdin.readline

# from collections import deque

# T = int(input())

# def next_move(i, number):
#     # D
#     if i == 0:
#         return (number * 2) % 10000, "D"
#     # S
#     elif i == 1:
#         return (10000 + number - 1) % 10000, "S"
#     # L
#     elif i == 2:
#         return (number * 10) % 10000 + (number // 1000), "L"
#     # R
#     elif i == 3:
#         return (number // 10) + ((number % 10) * 1000), "R"

# def BFS(A, B):
#     """
#     A->B 최소 방법 찾는 함수
#     """
    
#     hash_table = [0] * 10000
    
#     q = deque()
#     q.append(A)
#     hash_table[A] = ""
    
#     while q:
#         current_num = q.popleft()
        
#         for i in range(4):
#             next_num, move = next_move(i, current_num)
#             if hash_table[next_num] == 0:
#                 hash_table[next_num] = hash_table[current_num] + move
#                 if next_num == B:
#                     return hash_table[B]
#                 q.append(next_num)
            
    

# for _ in range(T):
#     A, B = map(int,input().split())
#     print(BFS(A,B))

"""
=== 백준 9019번 코드 리뷰 ===

[문제 이해]
- A에서 B로 가는 최소한의 연산(명령어 길이)을 구하는데, BFS를 잘 활용하여 올바르게 접근했습니다.

[설계 프로세스 평가]
- 주석 작성 여부: O (새로운 접근 방식에 대한 코멘트 존재)
- 문제 분석 단계: 충분함 (BFS 최단 거리 탐색 적용)
- 자료구조 선택 근거: 명확함 (deque 활용)
- 알고리즘 설계: 구체적 (각 연산에 대해 next_move 분리, 배열에 경로 문자열 저장)
- 설계-구현 일치도: 일치

[현재 접근 방식]
- `deque`를 이용한 BFS 탐색
- `next_move` 함수를 작성하여 D, S, L, R 연산을 수학식(+, *, %, //)으로 치환
- `hash_table` 리스트를 방문 처리 및 동시에 경로(문자열) 저장용으로 사용

[분석 결과]
- 시간 복잡도: O(V + E) (V=10000, E=40000). 시간 복잡도는 이론상 맞습니다.
- 예상 결과: PyPy3로는 통과 가능하나, Python3 환경에서는 **시간 초과(TLE)**가 발생할 확률이 큽니다.

[힌트]
💡 아주 잘 개선하셨고 논리적으로 완벽한 BFS 탐색입니다! 최적화만 조금 더 하면 완벽합니다.
- 시간 초과 고려 1: 파이썬에서는 배열 안에서 매번 문자열을 더하게(`+`) 되면 메모리와 시간을 많이 소모합니다. 
- 시간 초과 고려 2: `while` 문 안에서 `next_move()`라는 함수를 최대 40,000번 호출하므로 오버헤드가 발생합니다. 함수 호출 대신 루프 안에 각 연산(D, S, L, R)을 직접 풀어 쓰는(인라인) 것이 빠릅니다.
- 시간 초과 고려 3: `if next_num == B:` 검사는 `if hash_table[next_num] == 0:`(미방문 검사) 내부에서 수행하는 것이 더 효율적입니다.

[설계 개선 제안]
- 만약 문자열 더하기 방식조차 시간을 잡아먹는다면, 배열 2개를 사용하여 역추적(Backtracking)을 할 수 있습니다. `parent[next_num] = current_num`(어디서 왔는지), `move[next_num] = 연산자`(어떤 연산을 했는지)를 저장한 후, 목표점 B에 도달하면 부모를 계속 타고 올라가서 정답 배열을 뒤집는 방식도 학습해 보세요!

[더 알아보면 좋을 것]
- BFS에서 경로를 역추적(Backtracking tracing)하는 방법
- PyPy3와 Python3의 실행 속도 차이 (알고리즘 문제 풀이 시 PyPy3의 활용)
"""

# import sys
# input = sys.stdin.readline

# from collections import deque

# T = int(input())

# def find_path(parent_table, A, B):
#     """
#     출력값 찾는 함수
#     """
#     q = deque()
#     q.append(B)
#     answer = ""
    
#     while q:
#         current = q.popleft()
        
#         if current == A:
#             return answer
        
#         next_num = parent_table[current][0]
#         answer = parent_table[current][1] + answer
        
#         q.append(next_num)
    

# def BFS(A, B):
#     """
#     A->B 최소 방법 찾는 함수
#     """
    
#     parent_table = [0] * 10000
    
#     q = deque()
#     q.append(A)
#     parent_table[A] = [0,0]
    
#     while q:
#         current_num = q.popleft()
        
#         next_num = (current_num * 2) % 10000
#         if parent_table[next_num] == 0:
#                 parent_table[next_num] = [current_num,"D"]
#                 if next_num == B:
#                     return find_path(parent_table, A, B)
#                 q.append(next_num)
        
#         next_num = (10000 + current_num - 1) % 10000
#         if parent_table[next_num] == 0:
#                 parent_table[next_num] = [current_num,"S"]
#                 if next_num == B:
#                     return find_path(parent_table, A, B)
#                 q.append(next_num)
                
#         next_num = (current_num * 10) % 10000 + (current_num // 1000)
#         if parent_table[next_num] == 0:
#                 parent_table[next_num] = [current_num,"L"]
#                 if next_num == B:
#                     return find_path(parent_table, A, B)
#                 q.append(next_num)
                
#         next_num = (current_num // 10) + ((current_num % 10) * 1000)
#         if parent_table[next_num] == 0:
#                 parent_table[next_num] = [current_num,"R"]
#                 if next_num == B:
#                     return find_path(parent_table, A, B)
#                 q.append(next_num)
    

# for _ in range(T):
#     A, B = map(int,input().split())
#     print(BFS(A,B))

"""
=== 백준 9019번 코드 리뷰 ===

[문제 이해]
- A에서 B로 변환하기 위한 최소 연산 횟수 및 경로 찾기

[설계 프로세스 평가]
- 주석 작성 여부: O (새로운 역추적 방식 도출 기재)
- 문제 분석 단계: 충분함 (BFS + 경로 역추적 완벽 적용)
- 자료구조 선택 근거: 명확함 (큐 활용)
- 알고리즘 설계: 구체적 (연산 인라인화 및 Backtracking 테이블 적용)
- 설계-구현 일치도: 일치

[현재 접근 방식]
- 이전 피드백을 잘 반영하여 함수 호출 오버헤드를 없애고, 루프 안에서 연산식을 직접(인라인) 계산하고 있습니다.
- `parent_table`에 `[부모노드, 연산자]` 리스트를 저장하고, `find_path` 함수를 호출하여 목적지에 도달했을 때만 역으로 경로를 복원(Backtracking)하는 방식을 사용했습니다.

[분석 결과]
- 시간 복잡도: 탐색 O(V), 연산 4개 O(E), 역추적 복원 O(최단경로길이) 
- 예상 결과: 통과 (파이썬에서 자주 발생하는 시간 초과 요인들을 훌륭하게 해결한 코드입니다!)

[힌트]
💡 이전 힌트를 완벽하게 이해하고 코드로 구현하셨네요! 수고하셨습니다.
- 매번 방문 노드마다 누적된 문자열을 생성하던 방식에서 벗어나 노드 간의 관계성만 저장한 후 나중에 한 번에 경로를 만들어낸 방식이 베스트 프랙티스입니다.
- 극한의 시간 최적화 팁 1: `parent_table`에 방문할 때마다 `[current_num, "연산"]` 형태의 리스트 객체를 **매번 생성**하게 됩니다. 이보다는 `parents = [-1]*10000`, `moves = [""]*10000` 처럼 데이터 성격에 따라 1차원 리스트를 두 개로 분리하시면 리스트 객체 생성 비용이 없어져 속도 튜닝에 큰 도움이 됩니다.
- 공간/구현 최적화 팁 2: `find_path` 함수 내부 역추적은 단순 "부모 추적"이므로 `deque`를 사용할 필요 없이, 단순 `while current != A:` 꼴의 구조가 더 직관적입니다.
- 파이썬 팁: 파이썬에서는 `%` 연산자가 음수에 대해서도 양수 나머지를 자동으로 반환합니다! 따라서 S 연산을 `(current_num - 1) % 10000` 로 적어도 똑같이 작동합니다.

[설계 개선 제안]
- 만약 리팩토링을 다시 하신다면 위에서 제안한 1차원 리스트 2개 전략과 While문을 이용한 깔끔한 경로 역추적을 적용해 보시기 바랍니다.

[더 알아보면 좋을 것]
- 파이썬의 리스트(튜플) 객체 생성 오버헤드와 1차원 배열들의 성능 차이
- 단순 Linked List 개념을 while문으로 탐색하는 방식
"""

# 현재 제출을 하더라도 시간초과 발생
# 찾아보니 지금 매 순간마다 parent_table을 초기화하고 있지만 초기화 할 필요가 없음

import sys
input = sys.stdin.readline

from collections import deque

T = int(input())

parent_table = [0] * 10000

def find_path(A, B):
    """
    출력값 찾는 함수
    """
    
    global parent_table
    
    q = deque()
    q.append(B)
    answer = ""
    
    while q:
        current = q.popleft()
        
        if current == A:
            return answer
        
        next_num = parent_table[current][0]
        answer = parent_table[current][1] + answer
        
        q.append(next_num)
    
def BFS(A, B):
    """
    A->B 최소 방법 찾는 함수
    """
    
    global parent_table
    
    q = deque()
    q.append(A)
    
    visit_table = [-1] * 10000
    
    while q:
        current_num = q.popleft()
        
        next_num = (current_num * 2) % 10000
        if visit_table[next_num] == -1:
                parent_table[next_num] = [current_num,"D"]
                if next_num == B:
                    return find_path(A, B)
                visit_table[next_num] = 1
                q.append(next_num)
        
        next_num = (10000 + current_num - 1) % 10000
        if visit_table[next_num] == -1:
                parent_table[next_num] = [current_num,"S"]
                if next_num == B:
                    return find_path(A, B)
                visit_table[next_num] = 1
                q.append(next_num)
                
        next_num = (current_num * 10) % 10000 + (current_num // 1000)
        if visit_table[next_num] == -1:
                parent_table[next_num] = [current_num,"L"]
                if next_num == B:
                    return find_path(A, B)
                visit_table[next_num] = 1
                q.append(next_num)
                
        next_num = (current_num // 10) + ((current_num % 10) * 1000)
        if visit_table[next_num] == -1:
                parent_table[next_num] = [current_num,"R"]
                if next_num == B:
                    return find_path(A, B)
                visit_table[next_num] = 1
                q.append(next_num)
    

for _ in range(T):
    A, B = map(int,input().split())
    print(BFS(A,B))