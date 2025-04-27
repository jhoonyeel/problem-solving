N = int(input())

res = 1
for x in range(2, N + 1):
  res *= x

cnt = 0
while True:
  if res % 10 == 0:
    cnt += 1
    res //= 10
    continue
  else:
    break
print(cnt)