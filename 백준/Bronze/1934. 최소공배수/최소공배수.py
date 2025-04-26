import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
  A, B = map(int, input().split())
  a, b = A, B
  while b != 0:
    a, b = b, a % b
  gcd = a
  print(A * B // gcd)