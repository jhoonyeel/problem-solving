import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []

n = int(input().rstrip())
for _ in range(n):
  command = input().rstrip()
  if command == 'L':
    if left:
      right.append(left.pop())
  elif command == 'D':
    if right:
      left.append(right.pop())
  elif command == 'B':
    if left:
      left.pop()
  else:
    left.append(command[-1])
print(''.join(left + right[::-1]))