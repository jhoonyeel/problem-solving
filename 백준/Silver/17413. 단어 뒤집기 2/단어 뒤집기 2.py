chars = list(input())

res = []
reverse_stack = []
is_tag = False
for idx, x in enumerate(chars):
  if x == '<':
    if reverse_stack:
      res.append(''.join(reverse_stack[::-1]))
      reverse_stack = []
    is_tag = True
    res.append(x)
  elif x == '>':
    is_tag = False
    res.append(x)
  elif is_tag:
    res.append(x)
  elif not is_tag and x.isalnum():
    reverse_stack.append(x)
  elif not is_tag and x == ' ':
    res.append(''.join(reverse_stack[::-1]))
    reverse_stack = []
    res.append(x)
if reverse_stack:
  res.append(''.join(reverse_stack[::-1]))
print(''.join(res))