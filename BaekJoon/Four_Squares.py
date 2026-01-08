
# 문제 분석: [Four Squares](https://www.acmicpc.net/problem/17626)
# 풀이 방법: 라그랑주 네 제곱수 정리 + 브루트포스
# 시간 복잡도: O(sqrt(N)) 레벨로 매우 빠름

# import sys
# import math

# input = sys.stdin.readline # 하나만 받을 땐 굳이 필요 없지만 습관적으로 사용 추천

# def is_square(n):
#     return int(math.sqrt(n)) ** 2 == n

# def solve(n):
#     # 1. n이 완전제곱수면 답은 1
#     if is_square(n):
#         return 1
    
#     # 2. n = i^2 + j^2 꼴인지 확인 (답이 2)
#     # i는 1부터 sqrt(n)까지만 확인하면 됨
#     for i in range(1, int(math.sqrt(n)) + 1):
#         if is_square(n - i**2):
#             return 2
            
#     # 3. n = i^2 + j^2 + k^2 꼴인지 확인 (답이 3)
#     for i in range(1, int(math.sqrt(n)) + 1):
#         for j in range(1, int(math.sqrt(n - i**2)) + 1):
#             if is_square(n - i**2 - j**2):
#                 return 3

#     # 4. 라그랑주 정리에 의해 남은 경우는 무조건 4
#     return 4

# if __name__ == "__main__":
#     number = int(input())
#     print(solve(number))








import math

def is_square(n):
    return int(math.sqrt(n)) ** 2 == n

def find_square(n):
    
    if is_square(n):
        return 1
    
    for i in range(1,int(math.sqrt(n))+1):
        if is_square(n-i**2):
            return 2
        
    for i in range(1, int(math.sqrt(n))+1):
        for j in range(1, int(math.sqrt(n-i**2))+1):
            if is_square(n - i**2 - j**2):
                return 3
    
    return 4



if __name__ == "__main__":
    number = int(input())
    print(find_square(number))