n = int(input())
seq = list(map(int, input().split()))

no_delete_dp = [0] * (n + 1)
no_delete_dp[1] = seq[0]

yes_delete_dp = [0] * (n + 1)
yes_delete_dp[1] = seq[0]

for i in range(2, n + 1):
  no_delete_dp[i] = max(no_delete_dp[i - 1] + seq[i - 1], seq[i - 1])
  yes_delete_dp[i] = max(yes_delete_dp[i - 1] + seq[i - 1], no_delete_dp[i - 1])
print(max(max(no_delete_dp[1:]), max(yes_delete_dp[1:])))