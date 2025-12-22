import sys

input = sys.stdin.readline

N = int(input())
numbers = map(int,input().split())

# 소수 개수
count = 0

for num in numbers:
    is_prime = True
    for i in range(2,(num//2)+1):
        if (num % (i)) == 0:
            is_prime = False
            break
    if num == 1:
        is_prime = False
    if is_prime == True:
        count += 1

print(count)