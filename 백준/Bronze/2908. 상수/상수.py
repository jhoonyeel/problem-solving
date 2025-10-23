A, B = input().split()
A = list(reversed(A))
B = list(reversed(B))
print(max(int(''.join(A)), int(''.join(B))))
