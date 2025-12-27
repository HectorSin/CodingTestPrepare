num_1, num_2 = map(int,input().split())

min_num = min(num_1,num_2)
max_num = max(num_1,num_2)

# 최대 공약수
max_gonyak = 1

for i in range(min_num-1):
    # i+2부터 진행
    if min_num % (i+2) == 0:
        if max_num % (i+2) == 0:
            max_gonyak = i+2

print(max_gonyak)

# 최소 공배수
print(max_gonyak * (min_num//max_gonyak) * (max_num//max_gonyak))