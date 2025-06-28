N = int(input())

dp = [False] * max(4, N + 1)
dp[1] = True
dp[2] = False
dp[3] = True

for i in range(4, N + 1):
  if dp[i - 1] and dp[i - 3]:
    dp[i] = False
  else:
    dp[i] = True
print('SK' if dp[N] else 'CY')