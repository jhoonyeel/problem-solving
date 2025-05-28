n = int(input())

el = [int(input()) for _ in range(n)]

dp = [[0] * 3 for _ in range(n + 1)]
dp[1][0] = 0
dp[1][1] = el[0]
dp[1][2] = 0

for i in range(2, n + 1):
  dp[i][0] = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
  dp[i][1] = (dp[i - 1][0]) + el[i - 1]
  dp[i][2] = (dp[i - 1][1]) + el[i - 1]
print(max(dp[n]))