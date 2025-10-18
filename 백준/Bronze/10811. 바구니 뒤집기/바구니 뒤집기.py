N, M = map(int, input().split())

seq = list(range(1, N + 1))
for _ in range(M):
  start, end = list(map(int, input().split()))
  seq = seq[:start - 1] + list(reversed(seq[start - 1:end])) + seq[end:]
print(*seq)