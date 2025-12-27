# [백준 1181] 단어 정렬 - Refactoring Feedback
# 문제 링크: https://www.acmicpc.net/problem/1181
#
# [문제 분석]
# 1. 입력: N개의 단어 (1 <= N <= 20,000)
# 2. 조건:
#    - 길이가 짧은 것부터
#    - 길이가 같으면 사전 순으로
#    - **중복된 단어는 하나만 남기고 제거** (현재 코드에서 누락됨)
# 3. 시간 복잡도: N=20,000이므로 O(N^2) 알고리즘은 위험할 수 있음 (Python 기준).
#               O(N log N)을 권장.
#
# [개선 포인트]
# 1. 중복 제거: 현재 리스트에 모든 입력을 받고 있습니다. set()을 사용하여 중복을 제거해야 합니다.
# 2. 정렬 알고리즘:
#    - Python의 기본 sort()는 Timsort로 O(N log N)이며 Stable Sort입니다.
#    - key=lambda x: (len(x), x)를 사용하면 길이 -> 사전순 정렬이 한 번에 가능합니다.
# 3. 현재 구현된 Quick Sort의 문제:
#    - 재귀 호출(quick_sort)이 while 반복문 내부에 있습니다. 이는 의도치 않은 동작(무한 루프 등)을 유발합니다.
#    - Quick Sort는 일반적으로 Unstable Sort이므로, 앞서 수행한 사전순 정렬(Line 7)이 깨질 수 있습니다.

N = int(input())

word_list = list(set([input() for i in range(N)]))

word_list.sort(key=lambda x: (len(x), x))

for word in word_list:
    print(word)