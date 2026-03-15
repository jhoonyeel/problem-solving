dots = [list(map(int, input().split())) for _ in range(3)]

min_x, max_x = float('inf'), float('-inf')
min_y, max_y = float('inf'), float('-inf')
for dot in dots:
  x, y = dot
  min_x = min(min_x, x)
  max_x = max(max_x, x)
  min_y = min(min_y, y)
  max_y = max(max_y, y)

candidates = [[min_x, min_y], [min_x, max_y], [max_x, min_y], [max_x, max_y]]

for c in candidates:
  if c not in dots:
    print(*c)