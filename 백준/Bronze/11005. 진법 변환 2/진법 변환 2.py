N, B = map(int, input().split())

pw = 0
while B ** pw <= N:
  pw += 1
pw -= 1

res = []
for i in range(pw, -1, -1):
  cur = N // B ** i
  N %= B ** i
  
  if cur >= 10:
    cur = chr(ord('A') + cur - 10)
  else:
    cur = str(cur)
  res.append(cur)

print(''.join(res))