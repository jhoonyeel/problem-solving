T = int(input())
MAX = 10000

dp = [0] * (MAX + 1)
dp[0] = 1   # 0을 만드는 방법은 1가지 (아무것도 안 쓰는 것)

# 동전(=1,2,3)을 차례대로 적용
for coin in [1, 2, 3]:
  for j in range(coin, MAX + 1):
    dp[j] += dp[j - coin]

for _ in range(T):
  n = int(input())
  print(dp[n])
