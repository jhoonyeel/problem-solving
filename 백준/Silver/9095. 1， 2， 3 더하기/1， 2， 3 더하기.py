t = int(input())

MAX = 11
dp = [0] * (MAX + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(t):
  n = int(input())
  
  for i in range(4, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
  print(dp[n])