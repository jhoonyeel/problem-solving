T = int(input())
for _ in range(T):
  A, B = input().split()
  
  is_valid = sorted(A) == sorted(B)
  if is_valid:
    print(f"{A} & {B} are anagrams.")
  else:
    print(f"{A} & {B} are NOT anagrams.")