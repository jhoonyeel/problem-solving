N = int(input())

res = 1
for x in range(2, N + 1):
  res *= x
print(res)