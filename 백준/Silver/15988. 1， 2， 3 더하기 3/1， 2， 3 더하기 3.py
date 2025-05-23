MOD = 1_000_000_009
MAX = 1_000_000

dp = [0 for _ in range(MAX + 1)]
dp[1] = 1
dp[2] = 2 
dp[3] = 4 
for i in range(4, MAX + 1):
  dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

T = int(input())
for _ in range(T):
  n = int(input())
  print(dp[n] % MOD)
