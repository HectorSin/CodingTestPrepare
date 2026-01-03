"""
떡볶이 떡 만들기
"""

"""

N, M = map(int,input().split())

d_list = list(map(int,input().split()))
d_list.sort(reverse=True)

for i in range(d_list[0]-1,0,-1):
    check_num = 0 # 다 자르고 남은 숫자
    cut_num = 0 # 기계에 세팅할 숫자
    for d in d_list: # 떡들 [큰수부터]
        if d < i: # 떡이 기계 숫자보다 적으면 끝
            break
        check_num += (d-i)
    if check_num >= M:
        cut_num = i
        break

print(cut_num)

"""

N, M = map(int,input().split())
d_list = list(map(int,input().split()))

start = 1
end = max(d_list)

result = 0

while start <= end:
    mid = (start + end)//2
    cut_sum = 0

    for d in d_list:
        if d > mid:
            cut_sum += (d - mid)

    if cut_sum < M:
        end = mid - 1
    
    else:
        result = mid
        start = mid + 1

print(result)