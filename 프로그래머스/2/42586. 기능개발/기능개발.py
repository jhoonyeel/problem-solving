## 문제 정리
# 앞에 있는 "작업"이 끝나기 전에 뒤에 작업은 미리 끝나도 배포 불가능
## 풀이
# 작업별로 걸리는 날짜 적기
# 순서대로 날짜처리. 되는 대로 합쳐서 return

def solution(progresses, speeds):
    GOAL = 100
    days = []
    for p, s in zip(progresses, speeds):
        remain = GOAL - p
        day = 0
        while remain - s * day > 0:
            day += 1
        days.append(day)
    print(days)
    res = []
    progressing = None
    deploy = 0
    for d in days:
        if not progressing:
            progressing = d
            deploy += 1
            continue
        
        if progressing >= d:
            deploy += 1
            continue
        
        res.append(deploy)
        progressing = d
        deploy = 1
    res.append(deploy)
    
    return res