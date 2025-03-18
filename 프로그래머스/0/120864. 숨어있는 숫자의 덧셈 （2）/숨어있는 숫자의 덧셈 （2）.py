def solution(my_string):
    blank_lst = [x if x.isdigit() else ' ' for x in my_string]
    combine_lst = ''.join(blank_lst).split(' ')
    return sum(int(x) for x in combine_lst if x)