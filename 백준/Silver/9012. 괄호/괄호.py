n = int(input())
lines = [input() for _ in range(n)]

for line in lines:
  stk = []
  is_valid = True
  for ch in line:
    if ch == '(':
      stk.append(ch)
    elif ch == ')':
      if stk:
        stk.pop()
      else:
        is_valid = False
        break
  if is_valid and len(stk) == 0:
    print('YES')
  else:
    print('NO')