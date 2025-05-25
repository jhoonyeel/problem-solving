N, M = map(int, input().split())

N_list = [list(map(int, input().split())) for _ in range(N)]
M_list = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
  for j in range(M):
    print(N_list[i][j] + M_list[i][j], end=' ')
  print()