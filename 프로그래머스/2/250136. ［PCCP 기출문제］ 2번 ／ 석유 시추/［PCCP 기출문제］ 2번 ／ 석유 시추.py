from collections import deque

def solution(land):
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    col_sum = [0] * m
    
    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc))
        visited[sr][sc] = True
        
        size = 1
        cols = set([sc])
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    if not visited[nr][nc] and land[nr][nc] == 1:
                        visited[nr][nc] = True
                        q.append((nr, nc))
                        size += 1
                        cols.add(nc)
        
        for c in cols:
            col_sum[c] += size
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
    
    return max(col_sum)