import sys
sys.setrecursionlimit(10**6)

N = int(input())
seq = list(map(int, input().split()))
target = seq[-1]

# dp[i][j] : i번째 수까지 계산해서 j를 만드는 경우의 수
dp = [[-1] * 21 for _ in range(N)]

def dfs(idx, cur, dp):
  if cur < 0 or cur > 20:
    return 0
  if idx == N - 1:
    return int(cur == target)
  if dp[idx][cur] != -1:
    return dp[idx][cur]

  res = dfs(idx + 1, cur + seq[idx], dp) + dfs(idx + 1, cur - seq[idx], dp)
  dp[idx][cur] = res
  return res

print(dfs(1, seq[0], dp))