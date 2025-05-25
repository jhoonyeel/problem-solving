MOD = 10_007

N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = 1
dp[1][4] = 1
dp[1][5] = 1
dp[1][6] = 1
dp[1][7] = 1
dp[1][8] = 1
dp[1][9] = 1

for i in range(2, N + 1):
  dp[i][0] = (dp[i - 1][0]) % MOD
  dp[i][1] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
  dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
  dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]) % MOD
  dp[i][4] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]) % MOD
  dp[i][5] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5]) % MOD
  dp[i][6] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6]) % MOD
  dp[i][7] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] + dp[i - 1][7]) % MOD
  dp[i][8] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] + dp[i - 1][7] + dp[i - 1][8]) % MOD
  dp[i][9] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4] + dp[i - 1][5] + dp[i - 1][6] + dp[i - 1][7] + dp[i - 1][8] + dp[i - 1][9]) % MOD
print(sum(dp[N]) % MOD)