cards = list(range(1, 21))

for _ in range(10):
  s, e = map(int, input().split())
  cards[s-1:e] = cards[s-1:e][::-1]
print(*cards)