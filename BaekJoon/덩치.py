N = int(input())

size_list = []

for i in range(N):
    height, weight = map(int, input().split())
    size_list.append([height, weight])

count_list = []

for size in size_list:
    count = 1
    for re_size in size_list:
        if re_size[0] > size[0] and re_size[1] > size[1]:
            count += 1
    count_list.append(count)

for each_count in count_list:
    print(each_count, end=" ")