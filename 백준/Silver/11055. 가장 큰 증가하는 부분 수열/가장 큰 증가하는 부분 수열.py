N = int(input())
Ai = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
  dp[i] = Ai[i - 1]
  for j in range(1, i + 1):
    if Ai[i - 1] > Ai[j - 1]:
      dp[i] = max(dp[i], dp[j] + Ai[i - 1])
print(max(dp))