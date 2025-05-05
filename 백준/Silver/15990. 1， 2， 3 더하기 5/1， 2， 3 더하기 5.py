import sys
input = sys.stdin.readline

MOD = 1_000_000_009
MAX = 100_000

dp = [[0] * 4 for _ in range(MAX + 1)]

dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

for i in range(4, MAX + 1):
  dp[i][1] = (dp[i - 1][2] + dp [i - 1][3]) % MOD
  dp[i][2] = (dp[i - 2][1] + dp [i - 2][3]) % MOD
  dp[i][3] = (dp[i - 3][1] + dp [i - 3][2]) % MOD

t = int(input())

for _ in range(t):
  n = int(input())
  print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)