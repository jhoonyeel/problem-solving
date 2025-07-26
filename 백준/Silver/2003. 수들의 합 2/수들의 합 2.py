N, M = map(int, input().split())
seq = list(map(int, input().split()))

count = 0
start = 0
end = 0
total = 0

while True:
    if total >= M:
        total -= seq[start]
        start += 1
    elif end == N:
        break
    else:
        total += seq[end]
        end += 1

    if total == M:
        count += 1

print(count)
