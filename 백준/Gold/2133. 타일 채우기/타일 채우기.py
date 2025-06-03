N = int(input())

dp = [0] * (N + 1)
dp[0] = 1
if N >= 2:
  dp[2] = 3

for i in range(4, N + 1, 2):
  dp[i] = dp[i - 2] * 3
  for j in range(0, i - 2, 2):
    dp[i] += dp[j] * 2

if N % 2 == 0:
  print(dp[N])
else:
  print(0)
