A, B, C = map(int, input().split())
D = int(input())

H, M, S = 24, 60, 60

C += D

B += C // S
C %= S

A += B // M
B %= M

A %= H

print(A, B, C)