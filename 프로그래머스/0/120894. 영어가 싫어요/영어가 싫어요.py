def solution(numbers):
    d = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    for x in d:
        numbers = numbers.replace(x, str(d[x]))
    return int(numbers)