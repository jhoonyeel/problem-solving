def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    # my_string = "bbawwbb"
    # overwrite_string = "XX"
    # XXawwXX. replace는 모두 바뀜.