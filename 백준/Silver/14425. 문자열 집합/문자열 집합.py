N, M = map(int, input().split())
S = set()
for _ in range(N):
  record = input()
  S.add(record)

checks = [input() for _ in range(M)]

cnt = 0
for el in checks:
  if el in S:
    cnt += 1
print(cnt)