A = input()
B = input()
C = input()

if "1" <= A[0] <= "9":
    D = int(A) + 3
elif "1" <= B[0] <= "9":
    D = int(B) + 2
elif "1" <= C[0] <= "9":
    D = int(C) + 1

if D % 3 == 0:
    # 3의 배수 O
    if D % 5 == 0:
        # 5의 배수 O
        print("FizzBuzz")
    else:
        print("Fizz")
else:
    # 3의 배수 X
    if D % 5 == 0:
        print("Buzz")
    else:
        print(D)
