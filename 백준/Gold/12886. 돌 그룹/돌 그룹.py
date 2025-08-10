import sys
sys.setrecursionlimit(1000000)

A, B, C = map(int, input().split())
S = A + B + C
if S % 3 != 0:
  print(0)
  exit()

MAX = 1500
visited = [[False]*(MAX+1) for _ in range(MAX+1)]

def dfs(a, b):
  a, b, c = sorted((a, b, S - a - b))
  if visited[a][b]:
    return False
  visited[a][b] = True
  if a == b == c:
    return True

  # 세 쌍 (a,b), (a,c), (b,c)에 대해 연산
  for x, y in ((a,b), (a,c), (b,c)):
    if x == y: 
      continue
    # x<y가 되게 잡고 (2x, y-x)
    if x < y:
      nx, ny = x+x, y-x
      nz = S - nx - ny
      na, nb = sorted((nx, ny))  # 정규화는 dfs 들어갈 때 다시 수행됨
      if dfs(na, nb):
        return True
  return False
print(1 if dfs(A, B) else 0)