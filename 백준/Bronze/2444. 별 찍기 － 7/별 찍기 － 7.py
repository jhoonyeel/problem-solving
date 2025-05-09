N = int(input())

for i in range(2 * N - 1):
  space = abs(N - 1 - i)
  star = 2 * (N - space) - 1
  print(' ' * space + '*' * star)
