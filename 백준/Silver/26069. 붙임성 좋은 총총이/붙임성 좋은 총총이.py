N = int(input())
DEFAULT = "ChongChong"

s = set()
for _ in range(N):
  A, B = input().split()
  if A == DEFAULT or B == DEFAULT:
    s.add(A)
    s.add(B)
  elif A in s or B in s:
    s.add(A)
    s.add(B)
print(len(s))