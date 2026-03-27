import sys
input = sys.stdin.readline

N = int(input())
board = [[0]*1001 for _ in range(1001)]
papers = []

# 1. 색종이 덮기 (마지막에 덮인 색종이 번호 기록)
for i in range(1, N+1):
  x, y, w, h = map(int, input().split())
  papers.append((x, y, w, h))
  for r in range(y, y+h):
    for c in range(x, x+w):
      board[r][c] = i

# 2. 각 색종이별 "보이는 칸"만 다시 확인
res = [0]*(N+1)
for i in range(1, N+1):
  x, y, w, h = papers[i-1]
  cnt = 0
  for r in range(y, y+h):
    for c in range(x, x+w):
      if board[r][c] == i:
        cnt += 1
  res[i] = cnt

# 3. 출력
for i in range(1, N+1):
  print(res[i])