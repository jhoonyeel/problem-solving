n = int(input())
numbers = [int(input()) for _ in range(n)]

stk = []
op = []
going_up = 1
is_valid = True
for target in numbers:
  while target >= going_up:
    stk.append(going_up)
    op.append('push')
    going_up += 1
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