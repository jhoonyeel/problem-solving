import sys
input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
stk = []
res = [-1] * n
for i in range(n - 1, -1, -1):
  while stk and stk[-1] <= lst[i]:
    stk.pop()
  if stk:
    res[i] = stk[-1]
  stk.append(lst[i])
print(' '.join(map(str, res)))
