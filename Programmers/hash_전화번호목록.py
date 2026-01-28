"""
문제 설명
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

제한 사항
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.
입출력 예제
phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
입출력 예 설명
입출력 예 #1
앞에서 설명한 예와 같습니다.

입출력 예 #2
한 번호가 다른 번호의 접두사인 경우가 없으므로, 답은 true입니다.

입출력 예 #3
첫 번째 전화번호, “12”가 두 번째 전화번호 “123”의 접두사입니다. 따라서 답은 false입니다.

알림

2021년 3월 4일, 테스트 케이스가 변경되었습니다. 이로 인해 이전에 통과하던 코드가 더 이상 통과하지 않을 수 있습니다.
"""

# def solution(phone_book):
#     answer = True
#     sol_dic = {}
    
#     for pb in phone_book:
#         for i in range(len(pb)):
#             if pb[:i] in sol_dic:
#                 return False
    
#         sol_dic[pb] = 1
    
#     return answer

"""
=== Programmers 전화번호 목록 코드 리뷰 ===

[문제 이해]
- 전화번호부에 적힌 번호 중, 한 번호가 다른 번호의 접두어인지 확인하는 문제입니다.

[현재 접근 방식]
- 모든 전화번호를 먼저 Hash Map(Dictionary)에 저장합니다.
- 각 전화번호의 모든 접두사를 생성하여 Hash Map에 존재하는지 확인합니다.

[분석 결과]
- 시간 복잡도: O(N * M) (N: 번호 개수, M: 번호 길이)
  - Hash Map 생성: O(N * M)
  - 접두사 확인: 각 번호 별 최대 M번 조회, Hash 조회 O(1) → O(N * M)
- 예상 결과: 통과 (매우 효율적임)
- 이유: 입력 순서와 상관없이 모든 번호에 대해 접두사 존재 여부를 정확히 판단합니다.

[힌트]
💡 아주 훌륭한 접근입니다!
- 데이터를 미리 '정리(Hash에 저장)'해두고 시작함으로써 O(1) 탐색의 이점을 완벽하게 활용했습니다.
- `range(len(pb))`를 사용하셔서 자기 자신이 아닌 접두사만 정확히 체크한 점도 좋습니다 (i가 0부터 len-1까지이므로).

[더 알아보면 좋을 것]
- 문자열 정렬(Sorting)의 특성과 `startswith` 메서드
- 해시(Hash)를 이용한 O(1) 탐색
"""

def solution(phone_book):
    answer = True
    sol_dic = {}
    for pb in phone_book:
        sol_dic[pb] = 0
    
    for pb in phone_book:
        for i in range(1,len(pb)):
            if pb[:i] in sol_dic:
                return False
    
    return answer


# zip, startswith 사용
def solution(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True

# 해쉬를 이용한 방식