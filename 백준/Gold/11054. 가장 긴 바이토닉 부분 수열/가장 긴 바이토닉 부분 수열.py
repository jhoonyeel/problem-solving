N = int(input())
Ai = list(map(int, input().split()))

dp_increase = [1] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, i):
        if Ai[j - 1] < Ai[i - 1]:
            dp_increase[i] = max(dp_increase[i], dp_increase[j] + 1)

dp_decrease = [1] * (N + 1)
for i in range(N, 0, -1):
    for j in range(N, i, -1):
        if Ai[j - 1] < Ai[i - 1]:
            dp_decrease[i] = max(dp_decrease[i], dp_decrease[j] + 1)

max_length = 0
for i in range(1, N + 1):
    max_length = max(max_length, dp_increase[i] + dp_decrease[i] - 1)
print(max_length)