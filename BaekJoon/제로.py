K = int(input())

stack = []

for _ in range(K):
    number = int(input())

    if number == 0: # 지울수 있는 수가 있다고 보장하기에 stack 체크 X
        stack.pop()
    
    else:
        stack.append(number)

print(sum(stack))