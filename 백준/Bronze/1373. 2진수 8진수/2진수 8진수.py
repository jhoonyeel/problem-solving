binary = input()

n = len(binary)
if n % 3 != 0:
  binary = '0' * (3 - (n % 3))+ binary

res = ''
for x in range(0, len(binary), 3):
  three_size = binary[x:x + 3]
  res += str(int(three_size, 2))
print(res)