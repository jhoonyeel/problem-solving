line = input()

line = line.replace('()', ' ').strip()
pipe = 0
cnt = 0
for x in line:
  if x == '(':
    pipe += 1
  if x == ' ':
    cnt += pipe
  if x == ')':
    cnt += 1
    pipe -= 1
print(cnt)