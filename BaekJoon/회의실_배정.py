# N개의 타임테이블
# 입력 데이터가 시작과 끝 데이터를 포함한 데이터
# 시작과 동시에 끝나기 가능 ex 7 7
# 확실하지 않지만 숫자가 겹치면 안됨 즘 7 8 -> 9 10 이건 되지만 7 8 -> 8 10은 안되는 듯
# 처음에 데이터를 읽을때 끝 시간이 시작시간보다 작은 경우의 예외 처리 필요
# 입력되는 데이터는 정렬되지 않은 상태

# 시간이니 결국 0~24까지의 시간 범위가 있을 것으로 예상
# 25가 넘어서는 케이스가 있을까? -> 만약그렇다면 5번째줄 처음 시간이 끝 시간보다 클 수도 있음 [해당 케이스는 우선 해당 문제에서 예외 처리]

# N의 범위는 100,000 이하
# DP테이블로 24개의 리스트를 만들고 각각 N개의 개수만큼 저장한다고 가정을 했을때 24*100,000 개의 데이터 [메모리 제한 128MB상 충분히 가능해 보임]
# 다시 문제를 읽어보니 시간은 2**31 까지 있어 해당 항식 제고 필요 [대략 1000000000]

# import sys
# from collections import deque

# input = sys.stdin.readline

# N = int(input())

# q = deque()

# for _ in range(N):
#     s_t, e_t = map(int,input().split())
#     q.append([s_t, e_t])

# time_table = []

# while q:
#     now = q.popleft() # 현재 시간
#     if not time_table: # 기존에 회의실 없으면 1개 추가
#         time_table.append([1, now[1]]) # 회의 개수, 끝나는 시간
#     else:
#         new_time = [[1,now[1]]]
#         for time in time_table:
#             if now[0] > time[1]: # 현재 시작 시간이 회의실 시간 끝나는 시간보다 클 경우 해당 time_table의 개수 + 1, 끝나는 시간 업데이트
#                 new_time.append([time[0]+1, now[1]])
#         time_table = new_time
# # time_table.sort(key=lambda x:x[0], reverse=True)
# # print(time_table[0][0])

"""                                                                                                   
  === 백준 1931번 코드 리뷰 ===                                                                         
                                                                                                        
  [문제 이해]                                                                                           
  - 겹치지 않게 회의를 최대 몇 개 선택할 수 있는지 구하는 문제입니다.                                   
  - 같은 시각 종료/시작은 허용됩니다. (끝나는 시간 == 다음 시작 시간 가능)                              
                                                                                                        
  [현재 접근 방식]                                                                                      
  - 입력 순서대로 회의를 보면서 가능한 경우를 `time_table`에 누적하고 있습니다.                         
  - 여러 경우의 수를 리스트에 계속 추가하는 방식입니다.                                                 
                                                                                                        
  [분석 결과]                                                                                           
  - 시간 복잡도: 최악의 경우 매우 크게 증가 (경우의 수 누적으로 비효율적)                               
  - `time_table`을 순회하면서 같은 리스트에 append하는 구조라, 의도보다 많은 상태를 탐색하게 됩니다.    
  - 문제 핵심 조건(끝 시간과 시작 시간이 같은 경우 허용)과 비교 연산이 맞는지도 다시 점검이 필요합니다. 
  - 예상 결과: 시간 초과 또는 오답 가능성이 높습니다.                                                   
                                                                                                        
  [힌트]                                                                                                
  💡 이 문제는 "모든 경우를 늘리는 방식"보다 "정렬 + 선택 기준"이 핵심입니다.                           
  - 어떤 기준으로 회의를 먼저 선택해야 이후 선택 가능 횟수가 최대가 될지 생각해보세요.                  
  - 입력 순서 자체는 정답과 무관합니다. 먼저 데이터를 정리하면 길이 보입니다.                           
  - 특히 "끝나는 시간" 관점에서 보면 선택 규칙이 단순해집니다.                                          
                                                                                                        
  [더 알아보면 좋을 것]                                                                                 
  - 그리디 알고리즘의 선택 기준 증명                                                                    
  - 정렬 기준을 2개(주/부 기준)로 둘 때의 의미                                                          
  """ 

import sys

input = sys.stdin.readline

n = int(input().strip())
meetings = [tuple(map(int,input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1],x[0]))

count = 0
end_time = 0

for start, end in meetings:
    if start >= end_time:
        count += 1
        end_time = end

print(count)