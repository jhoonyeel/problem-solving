import sys

MAX = 1_000_000
is_prime = [True] * (MAX + 1)
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
  if is_prime[i]:
    for j in range(i * i, MAX + 1, i):
      is_prime[j] = False

inputs = list(map(int, sys.stdin.read().split()))
for n in inputs:
  if n == 0:
    break
  
  is_possible = False
  for a in range(3, n // 2 + 1, 2):
    if is_prime[a] and is_prime[n - a]:
      is_possible = True
      break
  
  if is_possible:
    print(f"{n} = {a} + {n - a}")
  else:
    print("Goldbach's conjecture is wrong.")
