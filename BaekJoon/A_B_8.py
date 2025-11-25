"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

N = int(input())

for num, _ in enumerate(range(N)):
    A, B = map(int,input().split())
    print(f"Case #{num+1}: {A} + {B} = {A+B}")