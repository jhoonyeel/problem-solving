from collections import deque
from itertools import combinations
import copy

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(temp_board):
  q = deque()
  for i in range(N):
    for j in range(M):
      if temp_board[i][j] == 2:
        q.append((i, j))

  while q:
    x, y = q.popleft()
    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]
      if 0 <= nx < N and 0 <= ny < M and temp_board[nx][ny] == 0:
        temp_board[nx][ny] = 2
        q.append((nx, ny))
  
  return sum(row.count(0) for row in temp_board)

# 벽 세울 빈 칸 좌표 수집
candidates = [(i, j) for i in range(N) for j in range(M) if board[i][j] == 0]

max_safe = 0
for walls in combinations(candidates, 3):
  copied = copy.deepcopy(board)
  for x, y in walls:
    copied[x][y] = 1
  safe_zone = bfs(copied)
  max_safe = max(max_safe, safe_zone)

print(max_safe)