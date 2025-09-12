N = int(input())
Ai = list(map(int, input().split()))

dp = [1] * (N + 1)
# dp[i]: i번째 요소를 마지막으로 하는 부분 수열의 길이 최댓값

for i in range(1, N + 1):
  for k in range(1, i):
    if Ai[k - 1] > Ai[i - 1]:
      dp[i] = max(dp[i], dp[k] + 1)
print(max(dp))

# 발생할 수 있는 모든 경우
# 현재 바라보는 요소를 선택할지 말지 결정한다.
# (현재 바라보는 요소 < 부분 수열의 마지막 요소)
# 1. Yes
# 2. No