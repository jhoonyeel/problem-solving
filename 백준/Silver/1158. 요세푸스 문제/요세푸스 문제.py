N, K = map(int, input().split())
people = list(range(1, N + 1))

result = []
idx = 0
while people:
    idx = (idx + K - 1) % len(people)
    result.append(str(people.pop(idx)))

print(f"<{', '.join(result)}>")