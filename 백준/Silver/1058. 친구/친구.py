N = int(input())
board = [list(input()) for _ in range(N)]

cnt = [0] * N

for i in range(N):
    for j in range(i + 1, N):
        # i와 j가 친구이거나, 공통 친구가 존재하는 경우
        if board[i][j] == 'Y':
            cnt[i] += 1
            cnt[j] += 1
        else:
            for k in range(N):
                if k != i and k != j:
                    if board[i][k] == 'Y' and board[k][j] == 'Y':
                        cnt[i] += 1
                        cnt[j] += 1
                        break  # 공통 친구 한 명만 확인되면 충분

print(max(cnt))
