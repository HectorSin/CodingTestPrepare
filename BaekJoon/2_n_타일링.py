# 1s, 256mb
# 문제 주소: https://www.acmicpc.net/problem/11726
# 문제 분석: 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수 구하기
# 현재 접근: DP (Bottom-up), 공간 복잡도 O(1) 최적화 시도 중
# 핵심 원리: f(n) = f(n-1) + f(n-2) (피보나치 수열과 유사)

# 🚀 힌트 레벨 1: 로직 단순화
# 매 반복마다 조건문(if result >= 10007)을 확인하는 것보다,
# 매번 연산 결과에 % 10007을 적용하는 것이 코드가 더 깔끔하고 안전합니다.
# 파이썬은 큰 정수를 자동 처리하지만, 정석적인 알고리즘 풀이 습관을 위해 매 단계 나누기를 권장합니다.

n = int(input())

# 초기값 설정
first = 1 # f(1)
second = 2 # f(2)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    # 수정된 깔끔한 로직
    # 조건문 없이 매번 나머지 연산을 수행하여 숫자가 커지는 것을 방지하고 코드를 단순화합니다.
    for i in range(3, n + 1):
        result = (first + second) % 10007
        first = second
        second = result
    
    # 마지막 결과 출력
    print(result)