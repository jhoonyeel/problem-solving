from itertools import combinations_with_replacement
N, M = map(int, input().split())

seq = list(map(int, input().split()))

for comb in combinations_with_replacement(sorted(seq), M):
  print(*comb)