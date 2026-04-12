f_body, f_tail = input().split()
m_body, m_tail = input().split()

s = set([f_body, f_tail, m_body, m_tail])

srt = sorted(s)

for x in srt:
  for y in srt:
    print(x, y)