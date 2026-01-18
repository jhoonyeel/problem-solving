import sys

def get_divisors(n):
  res = []
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      res.append(i)

  return res

for line in sys.stdin:
  n = int(line.rstrip())
  if n == -1:
    break
  
  res = get_divisors(n)
  total = sum(res)
  if total == n:
    print(f"{n} = {' + '.join(map(str, res))}")
  else:
    print(f"{n} is NOT perfect.")