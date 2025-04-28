import sys
input = sys.stdin.readline

def uqlid(x, y):
  while y > 0:
    x, y = y, x % y
  return x

t = int(input())

for _ in range(t):
  line = list(map(int, input().split()))
  n, vals = line[0], sorted(line[1:])
  gcd_sum = 0
  for i in range(n - 1):
    for j in range(i + 1, n):
      gcd_sum += uqlid(vals[i], vals[j])
  print(gcd_sum)
