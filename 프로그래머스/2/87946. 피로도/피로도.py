def solution(k, dungeons):
    l = len(dungeons)
    visited = [False] * l
    
    res = 0
    def dfs(idx, cur):
        nonlocal res
        res = max(res, idx)
        
        for i, (minimum, spent) in enumerate(dungeons):
            if not visited[i]:
                if cur >= minimum:
                    visited[i] = True
                    dfs(idx + 1, cur - spent)
                    visited[i] = False
    
    dfs(0, k)
    
    return res