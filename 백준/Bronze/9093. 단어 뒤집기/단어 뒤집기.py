n = int(input())
lines = [input().split() for _ in range(n)]

for line in lines:
  reverse = [word[::-1] for word in line]
  print(' '.join(reverse))