## 문제 정리
# 앞에 있는 "작업"이 끝나기 전에 뒤에 작업은 미리 끝나도 배포 불가능
## 풀이
# 작업별로 걸리는 날짜 적기
# 순서대로 날짜처리. 되는 대로 합쳐서 return

## 오답
# 인덱스 순회를 통해, i, i+1 동시 접근. days를 뒤에서부터 비교했음.
# 이웃끼리만 비교하면 안됨. 기준이 되는 변수가 존재해야 함.
# 그래서 기준이 되는 변수를 정의함. 그러나 역전 순회의 경우, 미래의 작업이 기준이 되는 구조기 때문에 불가능한 풀이 구조임.

## 개선
# 조건을 만족하는 최소 정수 day를 하나씩 증가시키는 while문 대신
# -> 수식화하여 한번에 최소 정수 day 찾기.
# 1.222 횟수가 필요함.-> 2로 올림. 1.0 횟수가 필요함.-> 2로 올리지 않음.
# 수식으로 나타내면 day = (remain + s-1) // s

def solution(progresses, speeds):
    GOAL = 100
    days = []
    for p, s in zip(progresses, speeds):
        remain = GOAL - p
        day = (remain + s-1) // s
        days.append(day)

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
        else:
            res.append(deploy)
            progressing = d
            deploy = 1
    res.append(deploy)
    
    return res
