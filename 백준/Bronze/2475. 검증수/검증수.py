nums = list(map(int, input().split()))

res = 0
for x in nums:
  res += x ** 2
print(res % 10)