n = int(input())

is_in_company = {
  "enter": True,
  "leave": False,
}

logs = {}
for _ in range(n):
  name, entry = input().split()
  if name not in logs:
    logs.setdefault(name, entry)
  else:
    logs[name] = entry

res = []
for k, v in logs.items():
  if is_in_company[v]:
    res.append(k)

res.sort(key=lambda x: x, reverse=True)
print('\n'.join(res))