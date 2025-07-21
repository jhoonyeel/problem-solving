N, M = map(int, input().split())

def dfs(start, path):
  if len(path) == M:
    print(' '.join(map(str, path)))
    return
  
  for i in range(start, N + 1):
    dfs(i, path + [i])
dfs(1, [])