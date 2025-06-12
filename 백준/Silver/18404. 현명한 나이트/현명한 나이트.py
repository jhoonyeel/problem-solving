from collections import deque

N, M = map(int, input().split())
X, Y = map(int, input().split())
enemy = [list(map(int, input().split())) for _ in range(M)]

# 나이트가 이동할 수 있는 8가지 방향
can_go = [
  # 왼쪽 위
  (-1, -2), (-2, -1), 
  # 오른쪽 위
  (1, -2), (2, -1),
  # 왼쪽 아래
  (-2, 1), (-1, 2),
  # 오른쪽 아래
  (2, 1), (1, 2)
]

dist = [[-1] * (N + 1) for _ in range(N + 1)]
dist[X][Y] = 0

queue = deque()
queue.append([X, Y])

while queue:
  current_x, current_y = queue.popleft()

  for dx, dy in can_go:
    nx, ny = current_x + dx, current_y + dy

    if 1 <= nx <= N and 1 <= ny <= N and dist[nx][ny] == -1:
      dist[nx][ny] = dist[current_x][current_y] + 1
      queue.append([nx, ny])

print(' '.join(str(dist[x][y]) for x, y in enemy))