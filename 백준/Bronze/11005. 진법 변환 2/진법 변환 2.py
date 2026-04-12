N, B = map(int, input().split())

if N == 0:
  print(0)
else:
  digits = []
  while N > 0:
    r = N % B
    if r >= 10:
      digits.append(chr(55 + r))
    else:
      digits.append(str(r))
    N //= B
  print(''.join(reversed(digits)))