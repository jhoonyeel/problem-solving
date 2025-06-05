N, X = map(int, input().split())
Ai = list(map(int, input().split()))

res = [str(x) for x in Ai if x < X]
print(' '.join(res))