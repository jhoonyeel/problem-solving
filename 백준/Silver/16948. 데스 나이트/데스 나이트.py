from collections import deque

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

moves = [(-2, -1), (-2, +1), (0, -2), (0, +2), (+2, -1), (+2, +1)]

visited = [[False] * N for _ in range(N)]

def bfs(start_r, start_c):
  queue = deque()
  queue.append((start_r, start_c, 0))
  visited[start_r][start_c] = True

  while queue:
    x, y, dist = queue.popleft()

    if x == r2 and y == c2:
      return dist

    for dx, dy in moves:
      nx, ny = x + dx, y + dy

      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        visited[nx][ny] = True
        queue.append((nx, ny, dist + 1))

  return -1

print(bfs(r1, c1))