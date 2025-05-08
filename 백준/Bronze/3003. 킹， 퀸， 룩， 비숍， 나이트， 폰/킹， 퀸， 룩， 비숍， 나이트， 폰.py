chess = list(map(int, input().split()))
base = [1, 1, 2, 2, 2, 8]

res = []
for i, v in enumerate(base):
  res.append(v - chess[i])
print(' '.join(map(str, res)))