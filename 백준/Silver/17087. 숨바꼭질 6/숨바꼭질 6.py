import sys
input = sys.stdin.readline

def uqlid(x, y):
  while y > 0:
    x, y = y, x % y
  return x

N, S = map(int, input().split())
dots = list(map(int, input().split()))

distance = [abs(S - x) for x in dots]

res = distance[0]
for i in range(1, N):
  res = uqlid(res, distance[i]) 
print(res)