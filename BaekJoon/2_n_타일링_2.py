# n = int(input())

# dp_table = [0] * (n+1)

# dp_table[1] = 1
# dp_table[2] = 3

# if n >= 3:
#     for i in range(3,n+1):
#         dp_table[i] = ((dp_table[i-2] * 2) + (dp_table[i-1]))%10007

# print(dp_table[n])

n = int(input())

first = 1
second = 3

if n >= 3:
    for i in range(3,n+1):
        result = (first * 2 + second) % 10007
        first, second = second, result
    print(result)
elif n == 1:
    print(1)
elif n == 2:
    print(3)