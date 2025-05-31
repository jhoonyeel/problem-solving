N = int(input())
Ai = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
  dp[i] = 1
  for j in range(1, i + 1):
    if Ai[j - 1] > Ai[i - 1]:
      dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))