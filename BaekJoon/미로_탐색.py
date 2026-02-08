# 경로 탐색 문제
# BFS사용 [최단 경로 찾기에]
# 방문 횟수 2차원 리스트에 저장

import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())

graph = []

for _ in range(N):
    Ms = input().rstrip()
    graph.append(list(Ms))

visited_list = [[0] * M for _ in range(N)]

visited_list[0][0] = 1 # 해당 문제는 시작점 포함 계산하기에 1로 설정

q = deque()
q.append([0,0])

dx = [1,0,-1,0]
dy = [0,-1,0,1]

find_process = False

while q and not find_process:
    current_place = q.popleft()

    for i in range(4):
        next_x = current_place[0] + dx[i]
        next_y = current_place[1] + dy[i]

        if next_x == N-1 and next_y == M-1:
            visited_list[next_x][next_y] = visited_list[current_place[0]][current_place[1]] + 1
            find_process = True
            break
        
        if 0 <= next_x < N and 0 <= next_y < M and visited_list[next_x][next_y] == 0 and graph[next_x][next_y] == '1':
            visited_list[next_x][next_y] = visited_list[current_place[0]][current_place[1]] + 1
            q.append([next_x,next_y])

print(visited_list[N-1][M-1])

# 24분 소요 클리어

"""
=== 백준 2178번 코드 리뷰 ===

[문제 이해]
- N×M 크기의 미로에서 (1,1)에서 (N,M)까지 최단 경로를 찾는 문제입니다
- 1은 이동 가능, 0은 벽, 시작 위치도 카운트에 포함됩니다

[설계 프로세스 평가]
- 주석 작성 여부: O (간단한 설계 메모 있음)
- 문제 분석 단계: 보완 필요 (핵심만 파악, 제약 조건 분석 부족)
- 자료구조 선택 근거: 명확함 (BFS + deque + 2차원 방문 배열)
- 알고리즘 설계: 추상적 (구체적인 단계 설명 부족)
- 설계-구현 일치도: 일치

[현재 접근 방식]
- BFS를 사용하여 최단 경로 탐색
- visited_list에 각 위치까지의 거리를 저장
- 목적지 도달 시 즉시 종료하는 최적화 적용

[분석 결과]
- 시간 복잡도: O(N × M) - 각 칸을 최대 1번 방문
- 공간 복잡도: O(N × M) - graph와 visited_list
- 예상 결과: 통과 ✅

[힌트]
💡 완벽하게 해결하셨습니다!
- BFS는 최단 경로 문제에 최적의 선택입니다
- 조기 종료 로직(find_process)으로 불필요한 탐색을 줄였어요
- 방문 배열에 거리를 함께 저장하는 것도 효율적입니다

[설계 개선 제안]
다음 문제부터는 주석을 조금 더 구체화해보세요:

```python
[문제 분석]
- N×M 미로, (1,1) → (N,M) 최단 경로
- N, M 최대 100 → O(N×M) = 10,000 충분히 가능
- 시작점 포함 카운트

[자료구조 선택]
- BFS: 가중치 없는 그래프 최단 경로 보장
- deque: O(1) popleft 연산
- 2차원 visited: 방문 체크 + 거리 저장 동시 처리

[알고리즘]
1. (0,0)에서 시작, visited[0][0] = 1
2. 큐에서 현재 위치 꺼내기
3. 4방향 탐색 (상하좌우)
4. 유효 범위 + 미방문 + 이동 가능(1) → 큐 추가
5. 목적지 도달 시 종료

[복잡도]
- 시간: O(N×M)
- 공간: O(N×M)
```

[코드 품질 피드백]
✅ 좋은 점:
- `sys.stdin.readline` 사용으로 입력 최적화
- `rstrip()`으로 개행 문자 제거
- 조기 종료로 불필요한 연산 방지
- 변수명이 직관적 (current_place, next_x, next_y)

💡 미세 개선 포인트:
- `find_process` 플래그 없이도 구현 가능 (도달 시 바로 print 후 exit)
- `graph[next_x][next_y] == '1'` 대신 `graph[next_x][next_y] != '0'` 가능
- 하지만 현재 코드도 충분히 명확하고 효율적입니다!

[더 알아보면 좋을 것]
- DFS vs BFS: 왜 이 문제는 BFS가 필수인가?
  → DFS는 최단 경로를 보장하지 않음
- 가중치가 있는 그래프의 최단 경로: 다익스트라 알고리즘
- 0-1 BFS: 가중치가 0 또는 1인 특수한 경우

[종합 평가]
⭐⭐⭐⭐⭐ (5/5)
문제를 정확히 이해하고 최적의 알고리즘을 선택했습니다.
24분 안에 클리어한 것도 훌륭합니다!
다음 문제부터는 코드 작성 전 설계 주석을 조금 더 상세히 작성하면
더 복잡한 문제도 체계적으로 접근할 수 있을 거예요. 🎉
"""