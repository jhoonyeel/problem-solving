N = int(input())

for i in range(1, N + 1):
  print(' ' * (N - (i - 1) - 1), end='')
  for _ in range(i):
    print('*', end=' ')
  print()