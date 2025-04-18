n = int(input())
lines = [input() for _ in range(n)]

for line in lines:
  lst = line.split()
  reverse = [list(el)[::-1] for el in lst]
  print(' '.join([''.join(l) for l in reverse]))