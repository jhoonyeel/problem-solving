x, y = map(int, input().split())

end_31 = [1,3,5,7,8,10,12]
end_30 = [4,6,9,11]
end_28 = [2]

day_cnt = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

DAY_OF_THE_WEEK = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

day_idx = 0
if x == 1:
  day_idx = y % 7
  print(DAY_OF_THE_WEEK[day_idx])
else:
  day_idx = (sum(day_cnt[:x-1]) + y) % 7
  print(DAY_OF_THE_WEEK[day_idx])