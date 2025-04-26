import sys
input = sys.stdin.readline

n = int(input())
line = map(int, input().split())
cnt = 0
for x in line:
  if x == 2:
    cnt += 1
    continue
  if x == 1 or x % 2 == 0:
    continue
  is_prime = True
  for y in range(3, x):
    if x % y == 0:
      is_prime = False
      break
  if is_prime:
    cnt += 1
print(cnt)