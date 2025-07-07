import sys
input = sys.stdin.readline

N, M = map(int, input().split())

words = [input().strip() for _ in range(N)]

lst = [x for x in words if len(x) >= M]

cnt = {}
for x in lst:
  if x in cnt:
    cnt[x] += 1
  else:
    cnt[x] = 1

info = list(cnt.keys())

info.sort()

info.sort(key=lambda x: len(x), reverse=True)

info.sort(key=lambda x: cnt[x], reverse=True)

for word in info:
  print(word)