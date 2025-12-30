# 2s 128mb
# 문제 분석: https://www.acmicpc.net/problem/1966
# 0. 문제 개요: 중요도가 다른 문서들이 큐에 섞여 있을 때, 우선순위가 높은 문서가 뒤에 있다면 현재 문서를 뒤로 보냅니다. 특정 문서(M번째)가 몇 번째로 인쇄되는지 구하는 문제입니다.
# 1. 접근 방식: Deque를 사용하여 시뮬레이션 구현 (User Code Approach)
# 2. 복잡도: N <= 100이므로 O(N^2) 시뮬레이션도 충분히 통과 가능합니다.
# 3. 주요 포인트:
#    - 현재 문서보다 중요도가 높은 문서가 '하나라도' 있으면 뒤로 보냅니다.
#    - 이때, 문서를 중복해서 넣지 않도록 주의해야 합니다.

# 💡 힌트 레벨 1: 현재 코드의 21-27번 줄 논리를 확인해보세요.
#    반복문 안에서 `queue.append`가 실행되면, 중요도가 높은 문서가 여러 개일 때 어떤 일이 벌어질까요?
#    (현재 문서가 여러 번 복제되어 큐에 들어갈 위험이 있습니다)

# 💡 힌트 레벨 2: `any()` 함수를 활용하면 "나보다 중요한 문서가 하나라도 있는지" 쉽게 확인할 수 있습니다.
#    ex) `if any(cur[1] < q[1] for q in queue): ...` (튜플로 (m, priority) 관리 시)


import sys
from collections import deque

input = sys.stdin.readline

trial = int(input())

# N개의 테스트 케이스
for _ in range(trial):
    N, M = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    count = 0
    while queue:
        # 첫번째 숫자를 빼고 가장 중요도가 큰지 체크
        check_paper = queue.popleft()
        success = True # 인쇄 성공 여부
        M -= 1 # -1이라면 현재 체크중인 문서가 확인중

        if queue:
            # 📌 체크포인트: 매 반복마다 list(queue)를 생성하면 O(N)이 소요됩니다.
            # `any`를 쓰면 이 반복문을 깔끔하게 대체할 수 있습니다.
            for q in queue:
                if q > check_paper: # 큐에 현재 페이퍼보다 중요한 문서가 있는지 체크
                    if M == -1:
                        M = len(queue)
                    queue.append(check_paper)
                    success = False
                    break
        
        # check_paper 인쇄 성공
        if success:
            count += 1
            if M == -1:
                print(count)