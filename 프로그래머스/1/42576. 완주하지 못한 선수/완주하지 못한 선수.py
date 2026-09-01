## 오답
# 1. 일반 리스트 비교는 불필요한 정렬 필요
# 2. 그래서 딕셔너리 사용함. 그러나 중복 네이밍 정보 사라짐.
# 3. 따라서, {name: count} 정보를 저장함.
# 부록. Counter를 사용하면 Counter 객체 사이 빈도 연산 가능.
# 번외. 주로 사용되는 라이브러리
"""
collections.deque
heapq
collections.defaultdict
collections.Counter
itertools.combinations / permutations
bisect
"""

from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    
    res = p - c
    
    return next(iter(res)) # "원소가 하나뿐인 dict/Counter에서 그 key 하나 꺼내기"