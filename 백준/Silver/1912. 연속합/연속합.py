n = int(input())
A = list(map(int, input().split()))

current_sum = A[0]
max_sum = A[0]

for i in range(1, n):
  current_sum = max(A[i], current_sum + A[i])
  max_sum = max(max_sum, current_sum)
print(max_sum)