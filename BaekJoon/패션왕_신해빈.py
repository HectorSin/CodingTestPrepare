import sys
input = sys.stdin.readline

"""
# 문제 분석: 패션왕 신해빈 (https://www.acmicpc.net/problem/9375)
# 문제 요약: 주어진 의상들로 만들 수 있는 조합의 개수를 구하는 문제입니다. (같은 종류는 중복 착용 불가, 알몸 불가)
# 입력 조건: 테스트 케이스 수 <= 100, 의상의 수 n <= 30
# 현재 접근: 의상 종류 리스트와 개수 리스트를 병렬로 관리하며 선형 탐색 사용.
# 복잡도 분석: n이 최대 30이므로 O(n^2) 알고리즘도 약 900번 연산으로 충분히 빠릅니다.
# 
# 💡 개선 포인트 (Level 1):
# - 리스트 복수 개를 사용하기보다, 딕셔너리(Dictionary) 자료구조를 활용하면 코드가 더 직관적이고 효율적(O(N))이 됩니다.
# - { "headgear": 2, "eyewear": 1 } 형태의 데이터 구조를 떠올려보세요.
"""

tc = int(input())

for _ in range(tc):
    n = int(input())
    
    # 💡 힌트: 딕셔너리를 사용하면 아래 두 리스트를 하나로 합칠 수 있습니다.
    # 예: clothes = {}
    cloth_list = []
    cloth_count = [0]*30
    
    for _ in range(n):
        cloth, c_type = input().split()
        
        # 📌 체크포인트: 딕셔너리를 쓰면 이 검색 과정을 O(1)로 줄일 수 있습니다. (현재는 O(N))
        if c_type in cloth_list:
            cloth_count[cloth_list.index(c_type)] += 1
        else:
            cloth_list.append(c_type)
            cloth_count[cloth_list.index(c_type)] += 1
    
    count = 1
    # 💡 힌트: 딕셔너리의 values()만 순회하면 됩니다.
    for c in cloth_count:
        if c != 0:
            count = count*(c+1)

    print(count-1)
