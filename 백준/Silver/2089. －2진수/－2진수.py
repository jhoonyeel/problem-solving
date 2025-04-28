N = int(input())

if N == 0:
  print(0)
else:
  res = []
  while N != 0:
    N, mod = divmod(N, -2)
    if mod < 0:
      N += 1
      mod += 2
    res.append(str(mod))
  print(''.join(reversed(res)))