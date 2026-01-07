N = int(input())

edge = 2
for _ in range(N):
  edge = edge * 2 - 1
dots = edge * edge
print(dots)