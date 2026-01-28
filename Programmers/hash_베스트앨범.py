# https://school.programmers.co.kr/learn/courses/30/lessons/42579

# 장르별 2개의 mp3
# 장르 100개 미만
# 노래개수 10000 이하

def solution(genres, plays):    
    answer = []
    
    music_hash = {}
    music_counter_hash = {}
    
    for i in range(len(genres)):
        if genres[i] not in music_hash:
            music_hash[genres[i]] = []
            music_counter_hash[genres[i]] = 0
        
        music_hash[genres[i]].append((i,plays[i]))
        music_counter_hash[genres[i]] += plays[i]
    
    for data in music_hash:
        music_hash[data].sort(key= lambda x: (x[1], -x[0]), reverse=True)
    
    items = sorted(music_counter_hash.items(), key = lambda x: x[1], reverse=True)
    
    for item, count in items:
        if len(music_hash[item]) >= 2:
            answer.append(music_hash[item][0][0])
            answer.append(music_hash[item][1][0])
        else:
            answer.append(music_hash[item][0][0])
    
    return answer

"""
=== 프로그래머스 베스트앨범 코드 리뷰 ===

[문제 이해]
- 장르별로 가장 많이 재생된 노래를 최대 2개씩 모아 베스트 앨범을 출시하는 문제입니다.
- 우선순위: 1.많이 재생된 장르 -> 2.장르 내 많이 재생된 노래 -> 3.고유 번호가 낮은 노래

[현재 접근 방식]
- 해시(Dictionary)를 사용하여 장르별 노래 목록과 장르별 총 재생 횟수를 저장했습니다.
- `key=lambda x: (x[1], -x[0])`를 사용하여 재생 횟수는 내림차순, 고유 번호는 오름차순(음수 변환 이용)으로 **완벽하게 정렬** 조건을 구현했습니다.
- 장르 자체도 총 재생 횟수로 정렬하여 우선순위를 잘 지켰습니다.

[분석 결과]
- 시간 복잡도: O(N log N) (N: 노래의 개수)
- 예상 결과: **통과 (매우 효율적임)**

[힌트]
💡 수정해 주신 정렬 로직이 아주 훌륭합니다! 의도가 명확하고 정확합니다.

- **collections.defaultdict**: `if genres[i] not in music_hash:` 같은 초기화 코드를 `defaultdict`를 쓰면 더 간결하게 줄일 수 있습니다. (선택 사항)

[더 알아보면 좋을 것]
- `zip(genres, plays)`와 `enumerate`를 함께 사용하여 데이터를 묶는 방법
"""