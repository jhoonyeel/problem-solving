line = input()

n = len(line)
for i in range(0, n, 10):
  if i + 10 < n:
    print(line[i:i+10])
  else:
    print(line[i:])