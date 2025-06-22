board = [list(input()) for _ in range(5)]

res = ''
row_len_lst = [len(row) for row in board]
max_len = max(row_len_lst)

for col in range(max_len):
  for row in range(5):
    if col < row_len_lst[row]:
      res += board[row][col]
print(res)
