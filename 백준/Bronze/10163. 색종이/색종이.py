# 10163 색종이
import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*101 for _ in range(101)]
papers = []

for i in range(1, N+1):
  x, y, w, h = map(int, input().split())
  papers.append((x, y, w, h))
  for r in range(y, y+h):
    for c in range(x, x+w):
      board[r][c] = i

res = [0]*(N+1)
for r in range(101):
  for c in range(101):
    if board[r][c] != 0:
      res[board[r][c]] += 1

for i in range(1, N+1):
  print(res[i])