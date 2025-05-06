N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
  for j in range(i):
    if A[j] < A[i]:
      dp[i] = max(dp[i], dp[j] + 1)

biggest = max(dp)
print(biggest)

res = []
last = float('inf')
current_len = biggest
for i in range(N - 1, -1, -1):
  if A[i] < last and dp[i] == current_len:
    res.append(A[i])
    last = A[i]
    current_len -= 1
print(' '.join(reversed(list(map(str, res)))))