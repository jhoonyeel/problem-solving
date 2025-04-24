from collections import deque
import sys
input = sys.stdin.readline

q = deque()
d = {
  'push_front': lambda x: q.appendleft(x),
  'push_back': lambda x: q.append(x),
  'pop_front': lambda: q.popleft() if q else -1,
  'pop_back': lambda: q.pop() if q else -1,
  'size': lambda: len(q),
  'empty': lambda: 0 if q else 1,
  'front': lambda: q[0] if q else -1,
  'back': lambda: q[-1] if q else -1,
}

n = int(input())
for _ in range(n):
  cmd = input().split()
  if cmd[0] == 'push_front':
    d['push_front'](cmd[1])
  elif cmd[0] == 'push_back':
    d['push_back'](cmd[1])
  elif cmd[0] == 'pop_front':
    print(d['pop_front']())
  elif cmd[0] == 'pop_back':
    print(d['pop_back']())
  elif cmd[0] == 'size':
    print(d['size']())
  elif cmd[0] == 'empty':
    print(d['empty']())
  elif cmd[0] == 'front':
    print(d['front']())
  elif cmd[0] == 'back':
    print(d['back']())