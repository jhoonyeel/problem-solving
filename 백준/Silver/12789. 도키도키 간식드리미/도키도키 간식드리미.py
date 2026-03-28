from collections import deque

N = int(input())
tickets = deque(map(int, input().split()))

stk = []
target = 1

while tickets:
  if target != tickets[0]:
    stk.append(tickets.popleft())
  else:
    tickets.popleft()
    target += 1
  while stk:
    if stk[-1] == target:
      stk.pop()
      target += 1
    else:
      break

if not stk:
  print("Nice")
else:
  print("Sad")