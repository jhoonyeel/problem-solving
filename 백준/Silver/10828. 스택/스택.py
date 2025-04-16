n = int(input())
commands = [input() for _ in range(n)]

stk = []
d = {
  'push': lambda x: stk.append(x), 'pop': lambda: -1 if len(stk) == 0 else stk.pop(), 'size': lambda: len(stk),
  'empty': lambda: 1 if len(stk) == 0 else 0, 'top': lambda: -1 if len(stk) == 0 else stk[-1]
}

for command in commands:
  if 'push' in command:
    stack, arg = command.split()
    d[stack](int(arg))
    continue
  print(d[command]())