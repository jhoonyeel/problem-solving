N = int(input())

stk = []
for i in range(N):
  book = input()
  stk.append(book)

s = sorted(stk)
idx, cnt = 0, 0
for i, v in enumerate(sorted(stk)):
  if cnt < s.count(v):
    cnt = s.count(v)
    idx = i
print(s[idx])