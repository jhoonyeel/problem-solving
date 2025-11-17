asc = list(range(1, 9))
desc = list(range(8, 0, - 1))
line = list(map(int, input().split()))

if line == asc:
  print('ascending')
elif line == desc:
  print('descending')
else:
  print('mixed')