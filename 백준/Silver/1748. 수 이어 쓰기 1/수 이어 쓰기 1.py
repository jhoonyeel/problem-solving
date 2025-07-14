N = int(input())

digit = 1
start = 1
result = 0

while True:
  end = start * 10 - 1
  if N <= end:
    result += (N - start + 1) * digit
    break
  result += (end - start + 1) * digit
  start *= 10
  digit += 1
print(result)