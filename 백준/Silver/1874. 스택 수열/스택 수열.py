n = int(input())
numbers = [int(input()) for _ in range(n)]

stk = []
op = []
start = 1
is_valid = True
for target in numbers:
  if target >= start:
      for x in range(start, target + 1):
          stk.append(x)
          op.append('push')
      start = target + 1
  if stk and stk[-1] == target:
      stk.pop()
      op.append('pop')
  else:
      is_valid = False
      break

if is_valid:
  for x in op:
    if x == 'push':
      print('+')
    else:
      print('-')
else:
  print('NO')