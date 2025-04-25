a, b = map(int, input().split())

div = min(a, b)
while not (a % div == 0 and b % div == 0):
  div -= 1
print(div)
print(div * a // div * b // div)