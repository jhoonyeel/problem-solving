line = input()

n = len(line)
for i in range(0, n, 10):
  print(line[i:i+10])