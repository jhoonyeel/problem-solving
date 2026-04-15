line = input()

res = []
for ch in line:
  if 'A' <= ch <= 'Z':
    res.append(ch.lower())
  elif 'a' <= ch <= 'z':
    res.append(ch.upper())

print(''.join(res))