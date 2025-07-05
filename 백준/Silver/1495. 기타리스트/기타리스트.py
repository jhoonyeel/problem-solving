N, S, M = map(int, input().split())

Vol = list(map(int,input().split()))

dp = [[False] * (M + 1) for _ in range(N + 1)]
dp[0][S] = True

for i in range(N):
  for v in range(M + 1):
    if dp[i][v]:
      if v + Vol[i] <= M:
        dp[i + 1][v + Vol[i]] = True
      if v - Vol[i] >= 0:
        dp[i + 1][v - Vol[i]] = True

for v in range(M, -1, -1):
  if dp[N][v]:
    print(v)
    break
else:
  print(-1)