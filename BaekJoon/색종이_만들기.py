"""
https://www.acmicpc.net/problem/2630
"""

# 1s, 128mb
# N [2~128] 2**k

import sys
input = sys.stdin.readline

N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

# print(graph) # NxN 그래프 확인

# k가 7이하이기에 재귀함수의 깊이도 최악의 순간에도 7단계 이상으로 가지 않음 -> 재귀함수 사용

white = 0
blue = 0

def split_four(graph,s_row,e_row,s_col,e_col):
    """
    4가지 영역으로 나누는 함수 \n
    graph \n
    행 - s_row, e_row \n
    열 - s_col, e_col
    """
    global white, blue
    
    old_col = graph[s_row][s_col]
    success = True
    # 안의 모든 구성요소가 같은 색인지 확인
    for i in range(s_row, e_row+1):
        for j in range(s_col, e_col+1):
            cur_col = graph[i][j]
            if old_col != cur_col:
                success = False
                break
    
    if success:
        # 성공했다면
        if old_col == 0:
            white += 1
        elif old_col == 1:
            blue += 1
    else:
        # 다르다면 4개로 나눠 다시 split_four 실행
        # 1
        split_four(graph, s_row,((s_row+e_row+1)//2)-1,s_col,((s_col+e_col+1)//2)-1)
        # 2
        split_four(graph, s_row,((s_row+e_row+1)//2)-1,((s_col+e_col+1)//2),e_col)
        # 3
        split_four(graph, ((s_row+e_row+1)//2),e_row,s_col,((s_col+e_col+1)//2)-1)
        # 4
        split_four(graph, ((s_row+e_row+1)//2),e_row,((s_col+e_col+1)//2),e_col)

split_four(graph,0,N-1,0,N-1)

print(white)
print(blue)

# 제출 결과 실패

"""
=== 백준 2630번 코드 리뷰 ===

[문제 이해]
- NxN 종이를 4등분하며 모두 같은 색일 때까지 자르는 분할 정복 문제입니다.
- 하얀색과 파란색 색종이의 개수를 각각 구해야 합니다.

[현재 접근 방식]
- 재귀 함수(split_four)를 사용하여 영역을 4분할하고 있습니다.
- 이중 반복문을 통해 영역 내 색상이 동일한지 검사합니다.

[분석 결과]
- 시간 복잡도: O(N^2 log N) (각 깊이마다 전체 영역 스캔)
- N <= 128이므로 연산량은 충분합니다.
- 예상 결과: '틀렸습니다' (Index 범위 문제)

[힌트]
💡 반복문의 범위를 다시 확인해보세요.
- Python의 `range(start, end)`는 `end`를 포함하지 않습니다.
- 현재 코드: `for j in range(s_col, e_col):`
- `e_col`까지 검사해야 하는데, `e_col` 직전까지만 검사하고 있습니다.
- `range(s_col, e_col + 1)`로 변경해야 마지막 열까지 확인할 수 있습니다.

[추가 팁]
- `break`문은 가장 안쪽의 for문만 탈출합니다. `success = False`가 되면 바깥쪽 for문도 탈출하거나 함수를 바로 종료하는 것이 불필요한 연산을 줄이는 데 도움이 됩니다.
"""

# 38번째 줄 range 범위 오타로 인해 생긴 문제 -> 해결 완료