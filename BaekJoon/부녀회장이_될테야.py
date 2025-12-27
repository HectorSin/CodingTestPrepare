# [Backjoon Refactor Agent Feedback 2차]
# 분석: 
# 1. 로직 수정 완료: 초기화 범위, 리스트 복사, sum 범위가 올바르게 수정되었습니다.
# 2. 남은 오류: 마지막 출력 시 인덱스 에러(IndexError)가 발생합니다.
# 제안: 리스트의 마지막 요소를 출력하려면 인덱스를 수정해야 합니다.

case = int(input())

for i in range(case):
    # 몇층
    K = int(input())
    # 몇호
    N = int(input())
    
    floor_list = list(range(1,N+1))

    for floor in range(K):
        new_room = list(floor_list)
        for room in range(N):
            new_room[room] = sum(floor_list[:(room+1)])

        floor_list = new_room

    print(floor_list[N-1])

    
    
