import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs_stack(node):
  stack = [node]
  visited[node] = True
  while stack:
    cur = stack.pop()
    for nxt in graph[cur]:
      if not visited[nxt]:
        visited[nxt] = True
        stack.append(nxt)

visited = [False] * (N + 1)
cnt = 0
for vertex in range(1, N + 1):
  if not visited[vertex]:
    dfs_stack(vertex)
    cnt += 1
print(cnt)
