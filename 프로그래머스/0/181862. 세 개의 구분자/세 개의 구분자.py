def solution(myStr):
    not_in_abc_lst = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split(' ')
    lst = [x for x in not_in_abc_lst if x]
    return lst or ['EMPTY']