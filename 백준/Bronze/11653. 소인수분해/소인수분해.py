N = int(input())

MAX = int(N ** 0.5)
res = []

for x in range(2, MAX + 1):
  while N % x == 0:
    N //= x
    res.append(x)

if N > 1:
  res.append(N)

print('\n'.join(map(str, res)))