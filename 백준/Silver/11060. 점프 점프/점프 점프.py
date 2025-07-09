N = int(input())

Ai = list(map(int, input().split()))

INF = 1001
dp = [INF] * N
dp[0] = 0

for i in range(N):
  for j in range(1, Ai[i] + 1):
    if i + j < N:
      dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[N - 1] == INF:
  print(-1)  # 도달 불가
else:
  print(dp[N - 1])  # 최소 점프 수 출력