# (목적지, 이전 위치)
def solution(dirs):
    can_go = {
        'U': (0, -1),
        'D': (0, 1),
        'R': (1, 0),
        'L': (-1, 0)
    }
    record = set()
    def dfs(seq, prev_x, prev_y):
        if seq == len(dirs):
            return
        
        ch = dirs[seq]
        
        dx, dy = can_go[ch]
        nx, ny = prev_x + dx, prev_y + dy
        
        if not(-5 <= nx <= 5 and -5 <= ny <= 5):
            dfs(seq + 1, prev_x, prev_y)
        else:
            a = (nx, ny)
            b = (prev_x, prev_y)
            record.add(tuple(sorted((a, b))))
            dfs(seq + 1, nx, ny)
    dfs(0, 0, 0)
    
    return len(record)