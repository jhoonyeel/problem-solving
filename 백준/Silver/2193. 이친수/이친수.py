N = int(input())

MAX = 90
dp = [[0] * 2 for _ in range(MAX + 1)]

dp[1][0] = 0 # X
dp[1][1] = 1 # 1

dp[2][0] = 1 # 10
dp[2][1] = 0  # X

for i in range(3, N + 1):
  for j in range(0, 2):
    dp[i][0] = dp[i - 1][1] + dp[i - 1][0]
    dp[i][1] = dp[i - 1][0]
print(sum(dp[N]))