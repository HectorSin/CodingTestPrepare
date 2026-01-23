# 2s, 512mb

# N = int(input())

# num_list_origin = list(map(int,input().split()))

# num_list = sorted(list(set(num_list_origin)))
# num_dic = {}

# # 이진 탐색 방법으로 해당 숫자보다 앞에 몇개의 숫자가 있는지 체크
# def binary_location_search(num_list, start, end, target):
#     """
#     이진 탐색 \n
#     num_list 리스트 인자 \n
#     start 시작점 \n
#     end 끝점 \n
#     target 인덱스를 찾고 싶은 대상 \n
#     """
    
#     global current_location

#     if start > end:
#         return
    
#     mid_loc = (start + end) // 2

#     if num_list[mid_loc] == target:
#         current_location = mid_loc

#     if num_list[mid_loc] < target:
#         binary_location_search(num_list, mid_loc + 1, end, target)
#     elif num_list[mid_loc] >= target:
#         binary_location_search(num_list, start, mid_loc - 1, target)


# for num in num_list:
#     if num not in num_dic:
#         num_dic[num] = -1
    
#     current_location = -1
#     binary_location_search(num_list, 0, len(num_list)-1, num)
#     num_dic[num] = current_location

# print_list = [num_dic[i] for i in num_list_origin]
# print(*print_list)

"""
=== 백준 18870번 코드 리뷰 ===

[문제 이해]
- 수직선 위의 좌표 N개를 압축하는 문제입니다.
- 좌표 압축이란, 해당 좌표값보다 작은 서로 다른 좌표의 개수로 값을 대체하는 것입니다.

[현재 접근 방식]
- 중복을 제거하고 정렬한 리스트(num_list)를 만듭니다.
- 정렬된 리스트를 순회하며, 각 숫자의 위치(인덱스)를 이진 탐색으로 찾습니다.
- 그 결과를 dictionary에 저장하여 매핑합니다.

[분석 결과]
- 시간 복잡도: O(N log N) (정렬) + O(K log K) (루프 내 이진탐색)
  - K는 중복을 제거한 원소의 수 (K <= N)
  - 전체 복잡도는 O(N log N)으로 제한 시간 내 통과 가능합니다.
- 예상 결과: 통과

[힌트]
💡 불필요한 연산을 줄일 수 있습니다.
- `num_list`는 이미 '정렬'된 상태로 순회하고 있습니다.
- 정렬된 리스트의 i번째 원소가 곧 i보다 작은 서로 다른 숫자의 개수가 아닐까요?
- 이진 탐색 없이 `enumerate`를 사용하면 더 심플하게 구현할 수 있습니다.

[더 알아보면 좋을 것]
- `enumerate()` 내장 함수
- Dictionary Comprehension 문법
"""


N = int(input())

num_list_origin = list(map(int,input().split()))

num_list = sorted(list(set(num_list_origin)))
num_dic = {}

for idx, i in enumerate(num_list):
    if i not in num_dic:
        num_dic[i] = -1

    num_dic[i] = idx

print_list = [num_dic[i] for i in num_list_origin]
print(*print_list)