year = int(input())

is_yoonean = year % 4 == 0 and (year % 100 != 0  or year % 400 == 0)
res = 1 if is_yoonean else 0
print(res)