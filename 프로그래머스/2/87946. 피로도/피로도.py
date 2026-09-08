## 접근
# 하루에 한번 탐험 가능. 최대한 많이 탐험. -> 개발 요구사항으로 변환 필요
# 소비가 큰 것부터. But, 최소 필요 피로도 고려.
# 단순히 소비 피로도와 최소 피로도 고려한 정렬을 하려 했으나, 최소 피로도의 비교값(현재 피로도)이 앞선 선택에 의해 변화됨.
# 따라서, 첫 시점에서 전역적인 정렬이 불가함.
# dfs를 통해 상태를 저장하는 구조 고려.


## 오답
# 탐색이 끝난 후 visited 에서 방문 노드를 제거함. 호출 스택과 동일한 개념.
# A -> B -> C. visited: A,B,C
# A -> B. visited: A,B. -> C 노드(자식 포함)는 탐색이 완료되고 dfs 함수가 return 되었음을 나타냄.

# if idx == n + 1: 종료 조건은 dfs구조라고 항상 필요한게 아님.
# dfs의 역할은 가능한 많이 탐색.이고, 따라서 종료 조건은 "언제 더이상 탐색할 수 없는가"에 달려있음.

def solution(k, dungeons):
    n = len(dungeons)
    res = 0
    
    for start in range(n):
        visited = [False] * n
        def dfs(cur, idx, cnt):
            if idx == n + 1:
                return cnt
            
            if dungeons[idx][0] > cur:
                return cnt
            
            visited[idx] = True
            next_cnt = cnt + 1
            best = next_cnt
            for i in range(n):
                if not visited[i]:
                    child = dfs(cur - dungeons[idx][1], i, next_cnt)
                    best = max(best, child)
            visited[idx] = False
            
            return best
        
        cnt = dfs(k, start, 0)
        res = max(res, cnt)
    
    return res