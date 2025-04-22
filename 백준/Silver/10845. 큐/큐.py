from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

d = {
  'push': lambda x: queue.append(x),
  'pop': lambda: queue.popleft() if queue else -1,
  'size': lambda: len(queue),
  'empty': lambda: 0 if queue else 1,
  'front': lambda: queue[0] if queue else -1,
  'back': lambda: queue[-1] if queue else -1,
}

n = int(input().rstrip())
for _ in range(n):
  command = input().rstrip()
  if command.split()[0] == 'push':
    d['push'](command.split()[1])
  elif command == 'pop':
    print(d['pop']())
  elif command == 'size':
    print(d['size']())
  elif command == 'empty':
    print(d['empty']())
  elif command == 'front':
    print(d['front']())
  elif command == 'back':
    print(d['back']())