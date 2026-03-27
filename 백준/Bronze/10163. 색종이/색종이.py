import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*1001 for _ in range(1001)]

for i in range(1, N+1):
  x, y, w, h = map(int, input().split())
  for r in range(y, y+h):
    for c in range(x, x+w):
      board[r][c] = i

res = [0]*(N+1)
for r in range(1001):
  for c in range(1001):
    if board[r][c] != 0:
      res[board[r][c]] += 1

for i in range(1, N+1):
  print(res[i])