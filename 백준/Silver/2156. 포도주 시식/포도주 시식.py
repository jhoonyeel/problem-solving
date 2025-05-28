n = int(input())
drink = [int(input()) for _ in range(n)]

if n == 1:
  print(drink[0])
elif n == 2:
  print(drink[0] + drink[1])
else:
  dp = [0] * (n + 1)
  dp[1] = drink[0]
  dp[2] = drink[0] + drink[1]

  for i in range(3, n + 1):
    dp[i] = max(
      dp[i - 1],
      dp[i - 2] + drink[i - 1],
      dp[i - 3] + drink[i - 2] + drink[i - 1]
    )
  print(dp[n])