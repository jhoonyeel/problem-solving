from collections import Counter

text = input().upper()

counter = Counter(text)
most = counter.most_common()

two_pair = len(most) > 1 and most[0][1] == most[1][1]
if two_pair:
  print('?')
else:
  print(most[0][0])