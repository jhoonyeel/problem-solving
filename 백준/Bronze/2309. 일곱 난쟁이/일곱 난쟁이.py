SEVEN = 100
height_list = [int(input()) for _ in range(9)]

nine = sum(height_list)
delete_sum = nine - SEVEN

delete_x, delete_y = 0, 0
for i in range(9):
  for j in range(i + 1, 9):
    if height_list[i] + height_list[j] == delete_sum:
      delete_x = height_list[i]
      delete_y = height_list[j]
      break
  if delete_x != 0:
    break

height_list.remove(delete_x)
height_list.remove(delete_y)

height_list.sort()
for x in height_list:
  print(x)