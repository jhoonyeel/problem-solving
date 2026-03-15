S = input()

cnt = 0
s = set()
for length in range(len(S)):
  for start in range(len(S) - length):
    s.add(S[start:start+length+1])
print(len(s))