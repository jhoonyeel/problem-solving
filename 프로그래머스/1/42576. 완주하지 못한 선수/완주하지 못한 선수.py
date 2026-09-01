## 오답
# 일반 리스트 비교는 불필요한 정렬 필요
# 그래서 딕셔너리 사용함. 그러나 중복 네이밍 정보 사라짐.
# 따라서, {name, count} 정보를 저장함.

def solution(participant, completion):
    idx = 0
    d = {}
    for name in participant:
        d[name] = d.get(name, 0) + 1
    
    for name in completion:
        d[name] -= 1
    
    for k, v in d.items():
        if v > 0:
            return k