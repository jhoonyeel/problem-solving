CURRENT = 100
KEY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

N = int(input())
num_broken = int(input())
if num_broken > 0:
  broken_key = list(map(int, input().split()))
else:
  broken_key = []

possible_key = [x for x in KEY if x not in broken_key]

min_click = abs(N - CURRENT)

for length in range(1, 7):
    channels = ['']

    for _ in range(length):
        equal_length_level_channels = []
        for prefix in channels:
            for p_key in possible_key:
                equal_length_level_channels.append(prefix + str(p_key))
        channels = equal_length_level_channels  # 갱신

    for s in channels:
        channel = int(s)
        press_count = len(s) + abs(N - channel)
        min_click = min(min_click, press_count)

print(min_click)