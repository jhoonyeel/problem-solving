N, B = map(int, input().split())

if N == 0:
  print(0)
  exit()

p = 1
while B ** p <= N:
  p += 1

res = []
for i in range(p - 1, -1, -1):
  power = B ** i
  cnt = N // power
  N %= power
  if cnt >= 10:
    res.append(chr(55 + cnt))
  else:
    res.append(str(cnt))
print(''.join(res))