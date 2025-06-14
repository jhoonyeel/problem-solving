T = int(input())
for _ in range(T):
  n = int(input())
  top, bottom = list(map(int, input().split())), list(map(int, input().split()))
  
  dp = [[0] * 3 for _ in range(n + 1)]
  dp[1][0] = 0
  dp[1][1] = top[0]
  dp[1][2] = bottom[0]
  
  for i in range(2, n + 1):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + top[i - 1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + bottom[i - 1]
  print(max(dp[n]))