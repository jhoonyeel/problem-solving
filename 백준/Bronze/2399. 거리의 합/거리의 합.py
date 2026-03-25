import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

prefix = 0
answer = 0

for i in range(N):
  answer += arr[i] * i - prefix
  prefix += arr[i]

print(answer * 2)