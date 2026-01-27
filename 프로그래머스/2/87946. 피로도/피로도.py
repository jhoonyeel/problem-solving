def solution(k, dungeons):
    l = len(dungeons)
    visited = [False] * l
    
    res = 0
    def dfs(cnt, cur):
        nonlocal res
        res = max(res, cnt)
        
        for i, (minimum, spent) in enumerate(dungeons):
            if not visited[i]:
                if cur >= minimum:
                    visited[i] = True
                    dfs(cnt + 1, cur - spent)
                    visited[i] = False
    
    dfs(0, k)
    
    return res