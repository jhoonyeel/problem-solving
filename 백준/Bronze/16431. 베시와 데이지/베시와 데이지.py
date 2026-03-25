import sys
input = sys.stdin.readline

br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

bessie = max(abs(br - jr), abs(bc - jc))
daisy = abs(dr - jr) + abs(dc - jc)

if bessie < daisy:
  print("bessie")
elif bessie > daisy:
  print("daisy")
else:
  print("tie")