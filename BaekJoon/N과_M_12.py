"""
수열을 받는데 비내림차순으로 제작
-> a <= b <= c <= d 이를 만족하면 됨
추가적으로 숫자를 중복해서 사용 가능
그럼 오름차순으로 리스트를 정렬 및 중복 제거하는 함수 필요

DFS를 재귀적으로 사용해서 해결
"""


N, M = map(int,input().split())

num_list = list(map(int,input().split()))

def num_sort(num_list):
    """
    리스트 오름차순 정렬 및 중복 제거
    """
    num_list = sorted(num_list)
    
    sorted_list = []
    
    prev_num = 0
    
    for n in num_list:
        if n != prev_num:
            sorted_list.append(n)
            prev_num = n
    
    return sorted_list
    
num_list = num_sort(num_list)

def DFS(depth, index):
    """
    depth = 현재 깊이
    index = 현재 숫자 인덱스 [해당 인덱스 이상이 나와야함]
    """
    global work_list
    
    if depth == M:
        print(*work_list)
        return
        
    for i in range(index,len(num_list)):
        work_list.append(num_list[i])
        DFS(depth+1, i)
        work_list.pop()

work_list = []
DFS(0,0)