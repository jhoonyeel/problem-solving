n, m = map(int, input().split())

def count_2_5_in_factorial(n, cnt_val):
  cnt = 0
  while n >= cnt_val:
    bae_su_cnt = n // cnt_val
    cnt += bae_su_cnt
    n //= cnt_val
  return cnt

count_2 = count_2_5_in_factorial(n, 2) - (count_2_5_in_factorial(m, 2) + count_2_5_in_factorial(n - m, 2))
count_5 = count_2_5_in_factorial(n, 5) - (count_2_5_in_factorial(m, 5) + count_2_5_in_factorial(n - m, 5))
print(min(count_2, count_5))