chess = list(map(int, input().split()))
base = [1, 1, 2, 2, 2, 8]

res = []
for x, y in zip(base, chess):
  res.append(x - y)
print(' '.join(map(str, res)))